from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import re
import libcst as cst
from spellchecker import SpellChecker
import ast

spell = SpellChecker()

print("Geef een directory in! (./inzendingen)")
p = Path(input())

namen = sorted([subdirectory.name for subdirectory in p.iterdir()])
lijst = {naam: {naam2: [] for naam2 in namen if naam < naam2} for naam in namen}
anonimisatie = {f"Student{x+1}" : namen[x] for x in range(0, len(namen))}

studentFiles = {}

class commentVisitor(cst.CSTVisitor):
    def __init__(self) -> None:
        self.comments = set()
    
    def visit_Comment(self, node: cst.Comment) -> bool | None:
        self.comments.add(node.value)

class lexicalVisitor(cst.CSTVisitor):
    def __init__(self):
        self.lexical = set()

    def visit_SimpleString(self, node):
        words = re.split(r"\b", ast.literal_eval(node.value))
        for word in words:
            if word: #removes whitespaces
                self.lexical.add(word.lower().strip())

    def visit_Name(self, node):
        self.lexical.add(node.value)
        
class commentRemover(cst.CSTTransformer):
    def __init__(self) -> None:
        super().__init__()

    def leave_Comment(self, original, updated):
        return cst.RemoveFromParent()

        
if(p.is_dir):
    print("Directory bestaat")

    for subdirectory in p.iterdir():
        if subdirectory.is_dir(): 
            pythonFiles = list(subdirectory.glob('**/*.py'))

            if len(pythonFiles) == 1: 
                studentFiles[subdirectory.name] = pythonFiles[0].read_text()
            else:
                studentFiles[subdirectory.name] = "Onverwachte fileStructuur"

    for Student1 in studentFiles:
        student1_text = studentFiles[Student1]

        student_CommentRemover = commentRemover()

        student1_CommentVisitor = commentVisitor()
        cstStudent1 = cst.parse_module(student1_text)
        cstStudent1.visit(student1_CommentVisitor)

        modded_tree1 = cstStudent1.visit(student_CommentRemover)

        student1_LexicalVisitor = lexicalVisitor()
        cstSpellcheckStudent1 = cst.parse_module(student1_text)
        cstSpellcheckStudent1.visit(student1_LexicalVisitor)



        for Student2 in studentFiles:
            if Student2>Student1: 
                student2_text = studentFiles[Student2]

                student2_CommentVisitor = commentVisitor()
                cstStudent2 = cst.parse_module(student2_text)
                cstStudent2.visit(student2_CommentVisitor)
            
                modded_tree2 = cstStudent2.visit(student_CommentRemover)

                student2_LexicalVisitor = lexicalVisitor()
                cstSpellcheckStudent2 = cst.parse_module(student2_text)
                cstSpellcheckStudent2.visit(student2_LexicalVisitor)


                identicalComments = student1_CommentVisitor.comments & student2_CommentVisitor.comments
                lexical_Intersection = student1_LexicalVisitor.lexical & student2_LexicalVisitor.lexical
                misspelled = spell.unknown(lexical_Intersection)
                if student1_text == student2_text: 
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append("identiek dezelfde file!")
                elif identicalComments:
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append(f"zelfde comments: {identicalComments}")
                elif lexical_Intersection:
                    for x in misspelled:
                        if x.strip():
                            lijst[anonimisatie[Student1]][anonimisatie[Student2]].append(f"zelfde spellfouten: {misspelled}")
                if modded_tree1.deep_equals(modded_tree2):
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append(f"zelfde code")

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("output.txt")
print(template.render(lijst=lijst, anonimisatie=anonimisatie))
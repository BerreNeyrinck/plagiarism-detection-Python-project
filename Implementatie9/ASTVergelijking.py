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
            # studentFiles[subdirectory.name] = pythonFiles[0].read_text()
            studentFiles[subdirectory.name] =  [author.read_text() for author in pythonFiles] #implementatie 8
            
    for Student1 in studentFiles:
        student1_texts = sorted(studentFiles[Student1]) #becomes a list, found from the keyindex "student1"
        student_CommentRemover = commentRemover()


        for elem in student1_texts:

            student1_ast = ast.parse(elem)
            student1_CommentVisitor = commentVisitor()
            cstStudent1 = cst.parse_module(elem)
            cstStudent1.visit(student1_CommentVisitor)
            modded_tree1 = cstStudent1.visit(student_CommentRemover)

            student1_LexicalVisitor = lexicalVisitor()
            cstSpellcheckStudent1 = cst.parse_module(elem)
            cstSpellcheckStudent1.visit(student1_LexicalVisitor)


        for Student2 in studentFiles:
            if Student2>Student1: 
                student2_texts = sorted(studentFiles[Student2])
                student2_CommentVisitor = commentVisitor()

                for elem in student2_texts:
                    student2_ast = ast.parse(elem)
                    cstStudent2 = cst.parse_module(elem)
                    cstStudent2.visit(student2_CommentVisitor)
                    modded_tree2 = cstStudent2.visit(student_CommentRemover)
                    student2_LexicalVisitor = lexicalVisitor()
                    cstSpellcheckStudent2 = cst.parse_module(elem)
                    cstSpellcheckStudent2.visit(student2_LexicalVisitor)
                    identicalComments = student1_CommentVisitor.comments & student2_CommentVisitor.comments
                    lexical_Intersection = student1_LexicalVisitor.lexical & student2_LexicalVisitor.lexical
                    misspelled = spell.unknown(lexical_Intersection)

                    identical = True
                    zipped = zip(student1_texts, student2_texts)
                    
                for x, y in zipped:
                    if x != y:
                        identical = False
                    if identical:
                        lijst[anonimisatie[Student1]][anonimisatie[Student2]].append("identiek dezelfde file!")

                identical2 = True
                if ast.unparse(student1_ast) != ast.unparse(student2_ast):
                    identical2 = False
                if identical2:
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append("zelfde AST!")

                if identicalComments:
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append(f"zelfde comments: {identicalComments}")

                if lexical_Intersection:
                    for x in misspelled:
                        if x.strip():
                            lijst[anonimisatie[Student1]][anonimisatie[Student2]].append(f"zelfde spellfouten: {misspelled}")

                if modded_tree1.deep_equals(modded_tree2):
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append(f"zelfde code")

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("output.txt")
print(template.render(lijst=lijst, anonimisatie=anonimisatie))
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import re
import libcst as cst

print("Geef een directory in! (./inzendingen)")
p = Path(input())

namen = sorted([subdirectory.name for subdirectory in p.iterdir()])
lijst = {naam: {naam2: [] for naam2 in namen if naam < naam2} for naam in namen}
anonimisatie = {f"Student{x+1}" : namen[x] for x in range(0, len(namen))}

studentFiles = {}
pythonDirs = []

class commentVisitor(cst.CSTVisitor):
    def __init__(self) -> None:
        self.comments = set()
    
    def visit_Comment(self, node: cst.Comment) -> bool | None:
        self.comments.add(node.value)


if(p.is_dir):
    print("Directory bestaat")

    counter = 1
    for subdirectory in p.iterdir():
        if subdirectory.is_dir(): 
            pythonFiles = list(subdirectory.glob('**/*.py'))
            pythonDirs.append(pythonFiles[0])

            if len(pythonFiles) == 1: 
                    studentFiles[subdirectory.name] = pythonFiles[0].read_text()
            else:
                studentFiles[subdirectory.name] = "Onverwachte fileStructuur"
        counter += 1

    for Student1 in studentFiles:
        student1_text = studentFiles[Student1]
        print(studentFiles[Student1])

        student1_CommentVisitor = commentVisitor()
        cstStudent1 = cst.parse_module(student1_text)
        cstStudent1.visit(student1_CommentVisitor)
        # Student1Comments = getComments(python_files_student1) #implementatie 4

        for Student2 in studentFiles:
            if Student2>Student1: 

                student2_text = studentFiles[Student2]
                student2_CommentVisitor = commentVisitor()
                cstStudent2 = cst.parse_module(student2_text)
                cstStudent2.visit(student2_CommentVisitor)
                # Student2Comments = Student1Comments = getComments(python_files_student2) #implementatie 4 groups: Hash, Comments

                identicalComments = student1_CommentVisitor.comments & student2_CommentVisitor.comments
                if student1_text == student2_text: 
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append("identiek dezelfde file!")
                elif identicalComments:
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append(f"zelfde comments: {identicalComments}")

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("output.txt")
print(template.render(lijst=lijst, anonimisatie=anonimisatie))
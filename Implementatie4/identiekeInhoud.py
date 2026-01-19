from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import re


print("Geef een directory in! (./inzendingen)")
p = Path(input())

namen = sorted([subdirectory.name for subdirectory in p.iterdir()])
lijst = {naam: {naam2: [] for naam2 in namen if naam < naam2} for naam in namen}
anonimisatie = {f"Student{x+1}" : namen[x] for x in range(0, len(namen))}

studentFiles = {}
pythonDirs = []


def getComments(file):
    return re.findall("(?P<Hash>#)(?P<comment>.*)", file)

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
        python_files_student1 = studentFiles[Student1]
        print(studentFiles[Student1])
        Student1Comments = getComments(python_files_student1) #implementatie 4
        for Student2 in studentFiles:
            if Student2>Student1: 
                python_files_student2 = studentFiles[Student2]

                Student2Comments = Student1Comments = getComments(python_files_student2) #implementatie 4 groups: Hash, Comments

                if python_files_student1 == python_files_student2: 
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append("identiek dezelfde file!")

                elif Student1Comments == Student2Comments and Student1Comments != []:
                    lijst[anonimisatie[Student1]][anonimisatie[Student2]].append(f"zelfde comments: {Student1Comments[0][1]}")



environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("output.txt")
print(template.render(lijst=lijst, anonimisatie=anonimisatie))
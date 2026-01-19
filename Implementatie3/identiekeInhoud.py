from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import re

namen = sorted(["Berre Neyrinck","Vincent Nys","Kristof Michielsen","Bart Peeters"])
lijst = {naam: {naam2: [] for naam2 in namen if naam < naam2} for naam in namen}
anonimisatie = {f"Student{x+1}" : namen[x] for x in range(0, len(namen))}

studentFiles = {}
pythonDirs = []
authors = []
print("Geef een directory in! (./inzendingen)")

p = Path(input())
if(p.is_dir):
    print("Directory bestaat")

    counter = 1
    for dir in p.iterdir():
        if dir.is_dir():
            pythonFiles = list(dir.glob('**/*.py'))
            pythonDirs.append(pythonFiles[0])
            if len(pythonFiles) == 1: 
                authors.append(dir.name)
                with open (pythonFiles[0]) as f:
                    studentFiles[dir.name] = f.readline()
            else:
                studentFiles[dir.name] = "Onverwachte fileStructuur"
        counter += 1
    for count1,Student1 in enumerate(studentFiles, start = 0):
        python_files_student1 = studentFiles[Student1]
        for Student2 in studentFiles:
            if Student2>Student1:
                python_files_student2 = studentFiles[Student2]
                if python_files_student1 == python_files_student2:
                    try:
                        lijst[anonimisatie[Student1]][anonimisatie[Student2]].append("fout: identiek dezelfde file!")
                    except KeyError as e:
                        print(f"KeyError: {e}. This likely means the key combination does not exist in 'lijst'.")

# lijst = {naam: {naam2: [] for naam2 in namen if naam < naam2} for naam in namen} #wtf am i looking at and why does it work


environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("output.txt")

print(template.render(lijst=lijst, anonimisatie=anonimisatie))
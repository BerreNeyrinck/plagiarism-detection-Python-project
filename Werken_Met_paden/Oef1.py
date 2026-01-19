from pathlib import Path
print("geef een directory")

p = Path(input())

if(p.is_dir):
    print("Directory bestaat")
print(list(p.glob('**/*.py')))
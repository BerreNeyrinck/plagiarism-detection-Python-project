import re

while(True):
    print("geef een email op")
    m = re.match(r"(?P<naam>\w[a-z]*)(?P<provider>@+[a-z]*)(?P<TLD>.+[a-z]*)", input())
    try:
        if(m.group("provider") != None):
            print("dit is een werkende email.")
            print(f"naam: {m.group("naam")}, provider: {m.group("provider")}, TLD: {m.group("TLD")}")
            print(f"naam: {m.group(1)}, provider: {m.group(2)}, TLD: {m.group(3)}")
    except:
        print("deze mail klopt niet helemaal!")


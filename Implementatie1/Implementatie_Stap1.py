from jinja2 import Environment, FileSystemLoader

namen = ["student1","student2","Student3","Student4"]
commentaar = ["/","/","/","zelfde spelfout"]


# personDict = dict[namen, dict[namen, list[str]]] #list[str] = lijst met opmerkingen

namenSecDic = {namen[x]: [commentaar[0]] for x in range(0, len(namen))}


processed_Dict = {namen[y]: namenSecDic for y in range(0,len(namen))}

# print(processed_Dict)
# print(personDict)

# print(namenSecDic)
# print(namen)
# print(processed_Dict[1])

# lijst = {naam: {naam2: [] for naam2 in namen if naam < naam2} for naam in namen} #wtf am i looking at and why does it work
lijst = {naam: {naam2: [] for naam2 in namen if naam < naam2} for naam in namen}
auteurs = enumerate(lijst.keys())
environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("output.txt")


print(template.render(lijst = lijst, ))
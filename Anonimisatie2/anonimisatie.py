from jinja2 import Environment, FileSystemLoader

namen = sorted(["Berre Neyrinck","Vincent Nys","Kristof Michielsen","Bart Peeters"])
commentaar = ["/","/","/","zelfde spelfout"]
# lijst = {naam: {naam2: [] for naam2 in namen if naam < naam2} for naam in namen} #wtf am i looking at and why does it work


lijst = {naam: {naam2: [] for naam2 in namen if naam < naam2} for naam in namen}
anonimisatie = {f"student{x+1}" : namen[x] for x in range(0, len(namen))}

environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("output.txt")

# lijst["Berre Neyrinck"]["Bart Peeters"].append("Zelfde syntaxfout: /'eror'")

print(template.render(lijst=lijst, anonimisatie=anonimisatie))
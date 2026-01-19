import random
import json

class BuildingVisitor:
    def do_something_for_industrial(self, ind):
        print(ind.CO2)

    def do_something_for_residential(self, res):
        print(res.temperatuur)
        print(res.oppervlakte)

class XMLExportVisitor(BuildingVisitor): #inherited buildingVisitor 
    def __init__(self) -> None:
        super().__init__()

    def do_something_for_industrial(self, ind):
        with open('XML.xml', 'a') as file:
            file.write(f"{ind}: CO2 Level - {ind.CO2}\n")
    
    def do_something_for_residential(self, res):
        with open('XML.xml', 'a') as file:
            file.write(f"{res}: oppervlakte - {res.oppervlakte} temp - {res.temperatuur} \n")

class JSONExportVisitor(BuildingVisitor): #inherited buildingVisitor
    visitedNodes = 0
    def __init__(self) -> None:
        super().__init__()

    def do_something_for_industrial(self, ind):
        with open('JSON.json', 'a') as file:
            file.write(f"{ind}: CO2 Level - {ind.CO2}\n")
        self.visitedNodes += 1
    
    def do_something_for_residential(self, res):
        with open('JSON.json', 'a') as file:
            file.write(f"{res}: oppervlakte - {res.oppervlakte} temp - {res.temperatuur} \n")
        self.visitedNodes += 1


class Industrial:
    def __init__(self, CO2) -> None:
        self.CO2 = CO2

    def __repr__(self) -> str:
        return f"Industrial Building"

    def accept(self, visitor):
        visitor.do_something_for_industrial(self)

class Residential:
    def __init__(self, oppervlakte, temperatuur) -> None:
        self.oppervlakte = oppervlakte
        self.temperatuur = temperatuur

    def __repr__(self) -> str:
        return f"Residential Building"
    
    def accept(self, visitor):
        visitor.do_something_for_residential(self) 


def main():
    building_visitor = BuildingVisitor()
    XML_Visitor = XMLExportVisitor()
    JSON_Visitor = JSONExportVisitor()

    gebouw1 = Industrial(23.3)
    gebouw2 = Industrial(11.9)
    gebouw3 = Residential(40, 20)
    gebouw4 = Residential(70, 13)
    gebouw5 = Residential(120, 22)

    buildings = [gebouw1, gebouw2, gebouw3, gebouw4, gebouw5]

    for building in buildings:
        building.accept(XML_Visitor)
        building.accept(JSON_Visitor)

    with open('JSON.json', 'r') as file:
        print(file.readlines())

main()

#Important little tibit for self: in a nutshell a visitor is a class/object that contains methods for other classes
#the other classes then "accept" the visitor to let it use internal data to create an output :D
#so:
#   buildings is going to be a list of objects of both res/ind objects 
#   then make sure the classes of said objects have the required data inside them to "steal" with the visitor
#   Exports are just "with open() ladida write to (cake.xml)"
# you got this bud :)

#don't see the use of having a BuildingVisitor and inheriting from it if you aren't using
import libcst as cst
nodeList = []
class arithmaticVisualizer(cst.CSTVisitor):
    def __init__(self):
        pass

    def visit_Integer(self, node: cst.Integer):
        print(node.value) 
        nodeList.append(int(node.value))

        print(f"sum of stuff: {sum(nodeList)}")

expression = "1 + 2 / 4 + 7 * 3"

ParsedEx = cst.parse_expression(expression)

visitor = arithmaticVisualizer()
ParsedEx.visit(visitor)


#how would anyone find this?
#note: couldn't find the "quick start" in CST docs so just looked around.. Found this:

#class FooingAround(libcst.CSTVisitor):
    # def visit_FunctionDef(self, node: libcst.FunctionDef) -> bool:
    #     return "foo" not in node.name.value

    # def visit_SimpleString(self, node: libcst.SimpleString) -> None:
    #     print(node.value)

#deduced that cst.simplestring = int soooooooooo cst.Integer should be int..

#again titbit for self: parse_expression returns what can "practically" be seen as an object(?)
#doesn't have a visit function. Don't even understand my own code

#so in my words: parsed_EX has a method called "visit" somewhere which has <callback>.visit_integer
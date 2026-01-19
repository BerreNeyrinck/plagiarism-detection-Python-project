import libcst as cst

class MultiplicationOperandVisualizer(cst.CSTVisitor):
    def __init__(self):
        pass
    
    def visit_BinaryOperation(self, node: cst.BinaryOperation): #when encountering a binary op
        
        if isinstance(node.operator, cst.Multiply):
            print(node.operator)
            leftNode = node.left
            rightNode = node.right

            if isinstance(leftNode, cst.BinaryOperation): #if left is ()
                print(leftNode.node.left)
                print(leftNode.node.right)
            if isinstance(rightNode, cst.BinaryOperation): #if right is ()
                print(rightNode.node.left)
                print(leftNode.node.right)

            print(node.left.value)
            print(node.right.value)

    def visit_Integer(self, node: cst.Integer): #when encountering an int
        # print(node.value)
        pass

       
expression = "1 + 2 / 4 + 7 * (3 + 2)"

ParsedEx = cst.parse_expression(expression)

visitor = MultiplicationOperandVisualizer()
ParsedEx.visit(visitor)


#code rundown: find binary operation in parsedEx
#if operator is instance of CST.mult ( * ) 
# print said operator: Multiply (...) 
# print left node: Integer(Value = X, ...)
# print right node: Integer(Value = Y, ...)

# (X + Y) is counted as a SEPERATE binary operator. so this node is a l o t longer
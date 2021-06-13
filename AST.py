from scanner import Token
class AST(object):
    def accept(self, visitor):
        method_name = 'visit_{}'.format(self.__class__.__name__)
        visit = getattr(visitor, method_name)
        return visit(self)

class BinOpNode(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self) -> str:
        return f"BinOp({self.left}, {self.op}, {self.right})"

class VariableNode(AST):
    def __init__(self, name):
        self.name:str = name
    def __repr__(self) -> str:
        return f"Variable({self.name})"

class NumberNode(AST):
    def __init__(self, number):
        self.number = number
    def __repr__(self) -> str:
        return f"Number({self.number})"

class UnOpNode(AST):
    def __init__(self, op, factor):
        self.op = op
        self.factor = factor
    def __repr__(self) -> str:
        return f"UnOp({self.op}, {self.factor})"

class Visitor(object):
    pass

class Eval(Visitor):
    def visit_NumberNode(self, number):
        return number.number
    
    def visit_UnOpNode(self, unop):
        if unop.op == Token.SUB.name:
            return - int(unop.factor.accept(self))
        else :
            return int(unop.factor.accept(self))
    
    def visit_BinOpNode(self, binop):
        if binop.op == Token.DIV.name:
            return binop.left.accept(self) // binop.right.accept(self)
        elif binop.op == Token.MUL.name:
            return binop.left.accept(self) * binop.right.accept(self)
        elif binop.op == Token.SUB.name:
            return binop.left.accept(self) - binop.right.accept(self)
        elif binop.op == Token.ADD.name:
            return binop.left.accept(self) + binop.right.accept(self)
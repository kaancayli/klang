class AST(object):
    pass

class BinOpNode(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self) -> str:
        return f"BinOp({self.left}, {self.op}, {self.right})"

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
        return f"BinOp({self.op}, {self.factor})"

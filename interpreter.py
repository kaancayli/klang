from AST import BinOpNode, NumberNode, UnOpNode, Eval
from lexer import Lexer
from scanner import Token

class Interpreter:
    def __init__(self, lexer, prog):
        self.lexer = lexer
        self.prog = prog
    
    def term(self):
        node = self.factor()
        while self.lexer.next()[0] in (Token.MUL.name, Token.DIV.name):
            if self.lexer.next()[0] == Token.MUL.name:
                token = Token.MUL.name
                self.lexer.advance()
            elif self.lexer.next()[0] == Token.DIV.name:
                token = Token.DIV.name
                self.lexer.advance()
            node = BinOpNode(node, token, self.factor())
        return node
    
    def factor(self):
        node = None
        if self.lexer.next()[0] != Token.DIGIT.name:
            if self.lexer.next()[0] == Token.LPARENT.name:
                self.lexer.advance()
                node = self.expr()
                if self.lexer.next()[0] == Token.RPARENT.name:
                    self.lexer.advance()
                    return node
                else :
                    raise RuntimeError
            elif self.lexer.next()[0] in (Token.ADD.name, Token.SUB.name):
                token = self.lexer.next()[0]
                self.lexer.advance()
                return UnOpNode(token, self.factor())
            else:
                raise RuntimeError

        self.lexer.advance()
        return NumberNode(int(self.lexer.curr_token[1]))
    
    def expr(self):
        node = self.term()
        while self.lexer.next()[0] in (Token.ADD.name, Token.SUB.name):
            if self.lexer.next()[0] == Token.ADD.name:
                token = Token.ADD.name
                self.lexer.advance()
            elif self.lexer.next()[0] == Token.SUB.name:
                token = Token.SUB.name
                self.lexer.advance()
            node = BinOpNode(node, token, self.term())
        return node
    

if __name__ == '__main__':
    prog = '(3 + 4 * 9) / 3 * -+-7'
    lexer = Lexer(prog)
    interpreter = Interpreter(lexer, prog)
    ast = interpreter.expr()
    print(ast)
    result = ast.accept(Eval())
    print(result)

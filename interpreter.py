from AST import BinOpNode, NumberNode, UnOpNode, VariableNode, Eval
from lexer import Lexer
from scanner import Token

symbol_table = dict()

class Interpreter:
    def __init__(self, lexer, prog):
        self.lexer = lexer
        self.prog = prog
    
    def variable(self):
        if self.lexer.next()[0] is Token.IDENTIFIER.name:
            self.lexer.advance()
            return VariableNode(self.lexer.curr_token[1])
        else:
            raise RuntimeError

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
            elif self.lexer.next()[0] is Token.IDENTIFIER.name:
                id = self.lexer.next()[1]
                self.lexer.advance()
                return NumberNode(symbol_table[id])
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
    
    def stmt(self):
        if self.lexer.next()[0] is Token.SEMI_COL.name:
            self.lexer.advance()
            return
        while self.lexer.next()[0] is Token.IDENTIFIER.name:
            id = self.variable()
            if self.lexer.next()[0] is Token.ASSIGN.name:
                self.lexer.advance()
                result = self.expr().accept(Eval())
                symbol_table[id.name] = result
                if self.lexer.next()[0] is Token.SEMI_COL.name:
                    self.lexer.advance()
                else :
                    raise RuntimeError
            elif self.lexer.next()[0] is Token.SEMI_COL.name:
                self.lexer.advance()
                continue
            else:
                raise RuntimeError

    

if __name__ == '__main__':
    prog = 'a = (3 + 4 * 9) / 3 * -+-7; b = a; c = 2*a; d = a + 2*c;'
    lexer = Lexer(prog)
    interpreter = Interpreter(lexer, prog)
    ast = interpreter.stmt()
    print("Result:", symbol_table)


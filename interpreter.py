from lexer import Lexer
from scanner import Token

class Interpreter:
    def __init__(self, lexer, prog):
        self.lexer = lexer
        self.prog = prog
    
    def term(self):
        result = self.factor()
        while self.lexer.next()[0] in (Token.MUL.name, Token.DIV.name):
            if self.lexer.next()[0] == Token.MUL.name:
                self.lexer.advance()
                result = result * self.factor()
            elif self.lexer.next()[0] == Token.DIV.name:
                self.lexer.advance()
                result = result // self.factor()
        return result
    
    def factor(self):
        if self.lexer.next()[0] != Token.DIGIT.name:
            print('Error')
        self.lexer.advance()
        return int(self.lexer.curr_token[1])
    
    def expr(self):
        result = self.term()
        while self.lexer.next()[0] in (Token.ADD.name, Token.SUB.name):
            if self.lexer.next()[0] == Token.ADD.name:
                self.lexer.advance()
                result = result + self.term()
            elif self.lexer.next()[0] == Token.SUB.name:
                self.lexer.advance()
                result = result - self.term()
        return result
    

if __name__ == '__main__':
    prog = '3 + 4 * 9 / 3'
    lexer = Lexer(prog)
    interpreter = Interpreter(lexer, prog)
    print(interpreter.expr())
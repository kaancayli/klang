from scanner import Scanner

class Lexer:
    def __init__(self, prog):
        self.__scanner = Scanner()
        self.prog = prog
        self.tokens = self.__scanner.parse(prog)
        self.pos = -1
        self.curr_token = None
    
    def parse(self, prog):
        return self.__scanner.parse(prog)
    def next(self):
        if self.pos + 1 < len(self.tokens):
            return self.tokens[self.pos + 1]
        return ('EOF', None)
    def advance(self):
        self.pos += 1
        if self.pos  < len(self.tokens):
            self.curr_token = self.tokens[self.pos]



if __name__ == '__main__':
    lexer = Lexer()
    prog = 'lambda:num (a, b) -> a * b<='
    prog2 = """lambda:num (a) -> 
    { 
        if (a <= 2) {
            ret true
        }
        ret false
    }
    """
    prog3 = """
            struct{
                num a = 5.7;
            }
    """
    tokens = lexer.parse(prog)
    print(prog)
    print(tokens)
    tokens = lexer.parse(prog2)
    print(prog2)
    print(tokens)
    tokens = lexer.parse(prog3)
    print(prog3)
    print(tokens)
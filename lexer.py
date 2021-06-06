from scanner import Scanner

class Lexer:
    def __init__(self):
        self.__scanner = Scanner()
    
    def parse(self, prog):
        return self.__scanner.parse(prog)
    


if __name__ == '__main__':
    lexer = Lexer()
    prog = 'lambda:num (a, b) -> a * b<='
    prog2 = """lambda:num (a) -> 
    { 
        if (a <= 2) {
            ret true
        }
        ret false
    }"""
    tokens = lexer.parse(prog)
    print(prog)
    print(tokens)
    tokens = lexer.parse(prog2)
    print(prog2)
    print(tokens)
from enum import Enum

class Token(Enum):
    SPACE = ' '
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    COMMA = ','
    SEMI_COL = ';'
    COLON = ':'
    DOT = '.'
    GT = '>'
    LT = '<'
    LTE = '<='
    GRE = '>='
    EQ = '=='
    ASSIGN = '='
    EOL = '\n'
    TRUE = 'true'
    FALSE = 'false'
    LPARENT = '('
    RPARENT = ')'
    LSQUARE = '['
    RSQUARE = ']'
    LCURLY = '{'
    RCURLY = '}'
    IDENTIFIER = 'ident'
    NUMBER = 'number'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    FOR = 'for'
    NUM = 'num'
    STR = 'str'
    TYPE = 'type'
    LIST = 'list'
    MAP = 'map'
    SET = 'set'
    TUPLE = 'tuple'
    LAMBDA = 'lambda'
    RET = 'ret'
    NODE = 'node'
    ARROW = '->'


class Scanner:
    def __init__(self):
        self.__delimeters = {' ', '+', '-', '*', '/', ',', ';', '.', '>', '<', '=', '(', ')', '[', ']','{', '}', ':','\n'}
        self.__operators = {'+', '-', '*', '/', '>', '<'}
        self.__keywords = {'if', 'else', 'while', 'num', 'str', 
            'type', 'list', 'map', 'set', 'tuple', 'lambda', 'ret', 'node', 'for', 'true', 'false'}

    def __isDelimiter(self, seq:str):
        return seq in self.__delimeters

    def __isOperator(self, seq:str):
        return seq in self.__operators

    def __validIdentifier(self, seq:str):
        if (seq[0] == '0' or seq[0] == '1' or seq[0] == '2' or
            seq[0] == '3' or seq[0] == '4' or seq[0] == '5' or 
            seq[0] == '6' or seq[0] == '7' or seq[0] == '8' or
            seq[0] == '9' or self.__isDelimiter(seq[0]) == True):
            return False
        return True
    def __isComparator(self, seq:str):
        return seq == '==' or seq == '<=' or seq == '>='
    
    def __isArrow(self, seq:str):
        return seq == '->'

    def __isNumber(self, seq:str):
        i = 0
        for ch in seq:
            if (ch != '0' and ch != '1' and ch != '2' and 
                ch != '3' and ch != '4' and ch != '5' and 
                ch != '6'and ch != '7'and ch != '8' 
                and ch != '9' and ch != '.' or (ch == '-' and i > 0)):
                return False
            i += 1
        return True

    def __isKeyword(self, seq:str):
        return seq in self.__keywords


    def parse(self, seq:str):
        left, right = 0, 0
        tokens = []
        if(len(seq) == 0):
            return False
        while left <= right and right < len(seq):
            if right < len(seq) and not self.__isDelimiter(seq[right]) :
                right += 1
            
            if left == right and right < len(seq) and self.__isDelimiter(seq[right]):
                if self.__isOperator(seq[right]):
                    if right + 2 <= len(seq) and (self.__isComparator(seq[left:right + 2]) or self.__isArrow(seq[left:right + 2])):
                        right += 1
                        tokens.append((Token(seq[left:right + 1]).name, seq[left:right + 1]))
                    else :
                        tokens.append((Token(seq[right]).name, seq[right]))
                else :
                    tokens.append((Token(seq[right]).name, seq[right]))
                right += 1
                left = right
            elif right == len(seq) and left != right or left != right and self.__isDelimiter(seq[right]) :
                sub_seq = seq[left:right]
                if self.__isKeyword(sub_seq):
                    tokens.append((Token(sub_seq).name, sub_seq))
                elif self.__isNumber(sub_seq):
                    tokens.append((Token('number').name, sub_seq))
                elif self.__validIdentifier(sub_seq):
                    tokens.append((Token('ident').name, sub_seq))
                left = right
        return tokens
if __name__ == '__main__':
    prog = 'lambda:num (a, b) -> a * b<='
    prog2 = """lambda:num (a) -> 
    { 
        if (a <= 2) {
            ret true
        }
        ret false
    }"""
    scanner = Scanner()
    tokens = scanner.parse(prog)
    print(prog)
    print(tokens)
    tokens = scanner.parse(prog2)
    print(prog2)
    print(tokens)
delimeters = {' ', '+', '-', '*', '/', ',', ';', '>',  '<', '=', '(', ')', '[', ']','{', '}'}
operators = {'+', '-', '*', '/', '>', '<', '='}
keywords = {'if', 'else', 'while', 'num', 'str', 
            'type', 'list', 'map', 'set', 'tuple', 'proc', 'ret', 'node'}

def isDelimiter(seq:str):
    return seq in delimeters

def isOperator(seq:str):
    return seq in operators

def validIdentifier(seq:str):
    if (seq[0] == '0' or seq[0] == '1' or seq[0] == '2' or
        seq[0] == '3' or seq[0] == '4' or seq[0] == '5' or 
        seq[0] == '6' or seq[0] == '7' or seq[0] == '8' or
        seq[0] == '9' or isDelimiter(seq[0]) == True):
        return False
    return True

def isNumber(seq:str):
    i = 0
    for ch in seq:
        if (ch != '0' and ch != '1' and ch != '2' and 
            ch != '3' and ch != '4' and ch != '5' and 
            ch != '6'and ch != '7'and ch != '8' 
            and ch != '9' and ch != '.' or (ch == '-' and i > 0)):
            return False
        i += 1
    return True

def isKeyword(seq:str):
    return seq in keywords


def parse(seq:str):
    left, right = 0, 0
    tokens = dict()
    count = 0
    if(len(seq) == 0):
        return False
    while left <= right and right < len(seq):
        if right < len(seq) and not isDelimiter(seq[right]) :
            right += 1
        if left == right and right < len(seq) and isDelimiter(seq[right]):
            if isOperator(seq[right]):
                tokens[f"operator_{count}"] = seq[right]
            count += 1
            right += 1
            left = right
        elif right == len(seq) and left != right or left != right and isDelimiter(seq[right]) :
            sub_seq = seq[left:right]
            if isKeyword(sub_seq):
                tokens[f"keyword_{count}"] = sub_seq
                count += 1
            elif isNumber(sub_seq):
                tokens[f"number_{count}"] = sub_seq
                count += 1
            elif validIdentifier(sub_seq):
                tokens[f"identifier_{count}"] = sub_seq
                count += 1
            left = right
    return tokens
if __name__ == '__main__':
    prog = 'num a = 5, ananınamı, 7, if, else proc ret'
    tokens = parse(prog)
    print(tokens)
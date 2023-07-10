def solution(quiz):
    result = [bool(eval(l.split(" = ")[0]) == int(l.split(" = ")[1])) for l in quiz]
    return ["O" if b else "X" for b in result]
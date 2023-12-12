def solution(l, r):
    a = [i for i in range(l, r + 1) if (set(str(i))) == set(['0', '5']) or (set(str(i))) == set(['5'])]
    return a if a else [-1]
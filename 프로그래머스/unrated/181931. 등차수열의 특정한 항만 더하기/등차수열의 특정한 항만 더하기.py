def solution(a, d, included):
    prog = [a+d*i for i in range(len(included))]
    return sum([num for num, tf in zip(prog, included) if tf])
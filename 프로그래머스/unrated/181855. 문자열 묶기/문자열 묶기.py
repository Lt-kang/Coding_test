def solution(strArr):
    l = [len(i) for i in strArr]
    return max([l.count(i) for i in set(l)])
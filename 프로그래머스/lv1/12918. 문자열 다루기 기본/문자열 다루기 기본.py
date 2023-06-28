def solution(s):
    if not (len(s)==4 or len(s)==6): return False
    return False if False in [i.isdigit() for i in s] else True
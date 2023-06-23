def solution(a, b):
    odd = [1,3,5]
    if a in odd and b in odd: answer = a**2 + b**2
    elif a not in odd and b not in odd: answer = abs(a-b)
    else: answer = (a+b)*2
    return answer
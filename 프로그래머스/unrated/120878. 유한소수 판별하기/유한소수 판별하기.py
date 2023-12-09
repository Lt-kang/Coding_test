from math import gcd
def solution(a, b):
    n = gcd(a,b)
    b //= n
    
    i = 2
    answer = []
    while i <= b:
        if b % i ==0:
            b //= i
            answer.append(i)
            
        else:
            i += 1
    
    answer = set(answer)
    temp = set([2,5])
    
    return 1 if not (answer - temp) else 2
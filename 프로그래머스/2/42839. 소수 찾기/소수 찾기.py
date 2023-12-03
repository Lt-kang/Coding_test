from itertools import *


def checkPrime(n):
    if n==1 or n== 0: return False
    for i in range(2, int(n**0.5) + 1):
        if n%i==0: return False
    return True

def solution(n):
    list_ = list(n)
    length = len(list_)
    answer = []
    cnt = 0

    for i in range(1, length+1):
        table = permutations(list_, i)

        for w in table:
            answer.append(int(''.join(w)))

    answer = list(set(answer))

    for x in answer:
        if checkPrime(x): 
            print(x)
            cnt += 1
    return cnt




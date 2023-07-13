import math

def prime_num(num):
    if num==1: return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0: return False
    return True

def solution(n):
    return len([i for i in range(1,n+1) if prime_num(i)])
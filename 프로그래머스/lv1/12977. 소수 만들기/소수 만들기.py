from itertools import combinations

def prime_num(n):
    if n==1: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True

def solution(nums):
    tables = combinations(nums,3)
    n = [sum(table) for table in tables]
    return len([i for i in n if prime_num(i)])
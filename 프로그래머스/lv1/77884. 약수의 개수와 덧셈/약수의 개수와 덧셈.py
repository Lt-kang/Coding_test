from math import sqrt

def check_numbers(num):
    if sqrt(num)==int(sqrt(num)): return False
    return True

def solution(left, right):
    return sum([2*num*check_numbers(num) - num for num in range(left,right+1)])
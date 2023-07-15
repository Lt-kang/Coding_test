from math import gcd
def solution(n1, d1, n2, d2):
    n1 *= d2
    n2 *= d1
    d1 *= d2
    g = gcd((n1+n2),d1)
    return [(n1+n2)//g,d1//g]
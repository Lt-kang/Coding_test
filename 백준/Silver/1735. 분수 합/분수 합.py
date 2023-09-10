import sys
# input = sys.stdin.readline
from fractions import Fraction

n1, d1 = input().split()
n2, d2 = input().split()

answer = str(Fraction(int(n1),int(d1))+Fraction(int(n2),int(d2)))

print(answer.replace("/"," ") if "/" in answer else answer+" 1")
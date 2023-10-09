import sys; input = sys.stdin.readline
import math
from collections import deque

def round(num):
    return int(num) + (1 if num-int(num)>= 0.5 else 0)

n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
l = deque(l)

per = round(n*0.15)
if n>per*2:
    for i in range(per):
        l.popleft()
        l.pop()

    print(round(sum(l)/len(l)))
else:
    print(0)

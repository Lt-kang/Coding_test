from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

l = deque()
for i in range(n):
    t = list(map(int,input().split()))
    if t[0]==1:
        l.append(t[1])
    if t[0]==2:
        if l: print(l.pop())
        else: print(-1)
    if t[0]==3:
        print(len(l))
    if t[0]==4:
        if l: print(0)
        else: print(1)
    if t[0]==5:
        if l: print(l[-1])
        else:
            print(-1)

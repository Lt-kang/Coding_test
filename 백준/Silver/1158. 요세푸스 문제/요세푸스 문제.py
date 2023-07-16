from collections import deque
import sys

temp = deque()
ret = []

a, b = map(int, sys.stdin.readline().split())

for i in range(a):
    temp.append(i+1)

while temp:
    for i in range(b-1):
        temp.append(temp.popleft())
    ret.append(temp.popleft())

print("<",end='')
for i in range(len(ret)-1):
    print(f"{ret[i]}, ",end='')
print(f"{ret[-1]}>")

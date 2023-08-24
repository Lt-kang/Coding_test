import sys
input = sys.stdin.readline

n = int(input())
l = list()
for _ in range(n):
    t = int(input())
    if t==0: l.pop()
    else:
        l.append(t)

print(sum(l))


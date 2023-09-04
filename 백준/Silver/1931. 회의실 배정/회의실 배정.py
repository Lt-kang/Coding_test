import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort(key=lambda x: (x[1], x[0]))
l = deque(l)

# print(l)

answer = [l.popleft()]
for _ in range(n-1):
    t = l.popleft()
    if t[0] >= answer[-1][1]:
        answer.append(t)


print(len(answer))



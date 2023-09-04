import sys
import heapq

input = sys.stdin.readline


n = int(input())

answer = []
for _ in range(n):
    t = int(input())
    if t:
        heapq.heappush(answer, t)
    else:
        if answer: print(heapq.heappop(answer))
        else:
            print(0)


import sys
import heapq

input = sys.stdin.readline


n = int(input())

answer = []
for _ in range(n):
    t = list(map(int, input().split()))
    if t[0]==0:
        if answer: print(-heapq.heappop(answer))
        else:
            print(-1)
    else:
        for i in range(1,len(t)):
            heapq.heappush(answer, -t[i])


import sys
import heapq

input = sys.stdin.readline


n = int(input())

p = []
m = []
for _ in range(n):
    t = int(input())
    if t:
        if t<0:
            heapq.heappush(m, -t)
        elif t>0:
            heapq.heappush(p, t)
    else:
        if not p and not m:
            print(0)
        elif not p and m:
            print(-heapq.heappop(m))
        elif p and not m:
            print(heapq.heappop(p))
        elif p and m:
            if p[0] >= m[0]: 
                print(-heapq.heappop(m))
            else:
                print(heapq.heappop(p))



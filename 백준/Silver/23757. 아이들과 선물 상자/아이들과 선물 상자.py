import sys
import heapq

input = sys.stdin.readline


n, m = list(map(int, input().split()))

c = list(map(lambda x: int(x)*(-1), input().split()))
w = list(map(int, input().split()))


heapq.heapify(c)


answer = 1
for idx in range(m):
    t = -heapq.heappop(c)
    k = t-w[idx]
    if k<0:
        answer = 0
        break
    else:
        heapq.heappush(c, -k)
        

print(answer)
import heapq
import sys
input = sys.stdin.readline


N, M = list(map(int, input().split()))

l = list(map(int, input().split()))


Q = []
heapq.heapify(l)
heapq.heappush(Q, heapq.heappop(l))


for _ in range(N-1):
    t = heapq.heappop(l)
    if M >= ((t+0.5)-(Q[-1]-0.5)):
        pass
    else:
        heapq.heappush(Q, t)

print(len(Q))

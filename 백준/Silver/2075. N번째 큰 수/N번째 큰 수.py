import sys
import heapq

input = sys.stdin.readline


n = int(input())

answer = []
t = list(map(int, input().split()))
for i in range(len(t)):
    heapq.heappush(answer, t[i])
mx = max(answer)

for _ in range(n-1):    
    t = list(map(int, input().split()))
    for i in range(len(t)):
        if t[i] > mx:
            heapq.heappush(answer, t[i])
            heapq.heappop(answer)
            

print(heapq.heappop(answer))



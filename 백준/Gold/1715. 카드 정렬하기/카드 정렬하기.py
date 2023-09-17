import heapq
import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
heapq.heapify(l)

answer = 0
while len(l)>1:
    temp = heapq.heappop(l) + heapq.heappop(l)
    answer += temp
    heapq.heappush(l, temp)

print(answer)



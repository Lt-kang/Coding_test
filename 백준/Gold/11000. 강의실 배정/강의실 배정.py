import sys
import heapq

input = sys.stdin.readline


n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()



answer = []
heapq.heappush(answer, l[0][1])

for i in range(1,n):
    if l[i][0] < answer[0]:
        heapq.heappush(answer, l[i][1])
    else:
        heapq.heappop(answer)
        heapq.heappush(answer, l[i][1])



print(len(answer))



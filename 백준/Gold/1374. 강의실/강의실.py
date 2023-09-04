import sys
import heapq

input = sys.stdin.readline


n = int(input())
l = []
for _ in range(n):
    t = list(map(int, input().split()))
    heapq.heappush(l, [t[1], t[2]])

l.sort(key=lambda x : x[0])
# print(l)


answer = []
heapq.heappush(answer, l[0][1])


cnt = []
for i in range(1,n):
    # print(answer, l[i][0])
    if l[i][0] < answer[0]:
        heapq.heappush(answer, l[i][1])
    else:
        # while answer and l[i][0] >= answer[0]:
        #     heapq.heappop(answer)
        while True:
            if answer:
                if l[i][0] >= answer[0]: heapq.heappop(answer)
                else: heapq.heappush(answer, l[i][1]); break
            else:
                heapq.heappush(answer, l[i][1])
                break

    cnt.append(len(answer))

try:
    print(max(cnt))
except:
    print(1)
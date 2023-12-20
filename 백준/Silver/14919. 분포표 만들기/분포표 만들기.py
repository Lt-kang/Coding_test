import heapq as h


n = int(input())
list_ = list(map(float, input().split()))
h.heapify(list_)

answer = []
for i in range(1, n + 1):
    
    m = round((1/n) * i, 7)
    while True:
        if list_:
            t = h.heappop(list_)            
        else:
            print(len(answer), end=' ')
            answer = []
            break
        
        if t < m:
            h.heappush(answer, t)
        elif t >= m:
            h.heappush(list_, t)
            print(len(answer), end=' ')
            answer = []
            break

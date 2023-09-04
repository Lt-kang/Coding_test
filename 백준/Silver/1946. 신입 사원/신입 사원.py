import sys
input = sys.stdin.readline


# l[0] 기준 오름차순 정렬

t = int(input())
for _ in range(t):
    n = int(input())
    t = [0]*n
    for i in range(n):
        t[i] = list(map(int, input().split()))
    t.sort()
    st = t[0][1]
    cnt = 1
    for j in range(1,n):
        if t[j][1] < st: 
            cnt += 1
            st = t[j][1]
    print(cnt)

    
    
    
    

    



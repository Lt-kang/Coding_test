# n = 책의 개수 (0 <= 50)
# m = 최대 무게 (<= 1000)

n, m = map(int,input().split())

if n==0: 
    cnt = 0
elif n!=0: 
    cnt = 1
    temp = 0
    for i in list(map(int,input().split())):
        if temp + i <= m:
            temp += i
        elif temp + i > m:
            cnt += 1
            temp = i

print(cnt)
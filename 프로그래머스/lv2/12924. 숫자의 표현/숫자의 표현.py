def solution(n):
    cnt = 0
    for i in range(1,n+1):
        k = i+1
        while True:
            if (i+k)*(k-i+1)//2==n or i==n: cnt +=1; break
            elif (i+k)*(k-i+1)//2>n: break
            else: k += 1
    return cnt
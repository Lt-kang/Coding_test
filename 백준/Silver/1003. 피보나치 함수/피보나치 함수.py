n = int(input())


fibo = [[0,0]]*41
fibo[0] = [1,0]
fibo[1] = [0,1]
fibo[2] = [1,1]


for _ in range(n):
    t = int(input())
    
    if t>=3:
        for i in range(3,1+t):
            fibo[i] = [fibo[i-1][0]+fibo[i-2][0], fibo[i-1][1]+fibo[i-2][1]]
        print(f"{fibo[t][0]} {fibo[t][1]}")
    if t<3:
        print(f"{fibo[t][0]} {fibo[t][1]}")
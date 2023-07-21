n = int(input())



if n != 0:
    fibo = [0]*(n+1)
    fibo[1] = 1

    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    
    print(fibo[-1])

elif n==0: print(0)
elif n==1 or 2: print(1)

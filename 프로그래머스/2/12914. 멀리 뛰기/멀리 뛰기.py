def solution(n): 
    fibo = [1] * (n+1)
    for i in range(2, n+1):
        fibo[i] = sum(fibo[i-2:i])
    return fibo[-1]%1234567
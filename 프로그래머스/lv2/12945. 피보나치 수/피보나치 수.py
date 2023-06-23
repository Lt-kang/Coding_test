def solution(n):
    fibo = [0]*(n+1)
    fibo[1] = 1
    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[-1]%1234567

# 개선 코드(피보나치 수열의 더 간단한 코드)
# 바로 해석 가능하므로 주석은 달지 않음.
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
    return a

n = int(input())
fibo = [1]*n

for i in range(3, n):
    fibo[i] = fibo[i-1] + fibo[i-3]

print(fibo[-1])
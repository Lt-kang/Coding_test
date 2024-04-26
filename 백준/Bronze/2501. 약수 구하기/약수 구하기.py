N, K = map(int, input().split())

prime = []
for i in range(1, N+1):
    if N%i==0: prime.append(i)


print(prime[K-1] if len(prime) >= K else 0)
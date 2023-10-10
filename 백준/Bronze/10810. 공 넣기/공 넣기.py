


M, N = map(int, input().split())

bucket = [0]*M

for _ in range(N):
    i, j, k = map(int, input().split())
    for w in range(i-1,j):
        bucket[w] = k

bucket = [str(i) for i in bucket]
print(' '.join(bucket))

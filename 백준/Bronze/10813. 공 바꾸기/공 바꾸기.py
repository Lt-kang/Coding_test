


M, N = map(int, input().split())

bucket = [i for i in range(M+1)] 

for _ in range(N):
    i, j= map(int, input().split())
    bucket[i], bucket[j] = bucket[j], bucket[i]

bucket = [str(i) for i in bucket]
print(' '.join(bucket[1:]))



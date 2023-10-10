


M, N = map(int, input().split())

bucket = [i for i in range(M+1)] 

for _ in range(N):
    i, j= map(int, input().split())
    temp = bucket[i:j+1]
    temp.reverse()
    bucket[i:j+1] = temp
        

bucket = [str(i) for i in bucket]
print(' '.join(bucket[1:]))





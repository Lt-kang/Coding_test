import sys
input = sys.stdin.readline


N, M = list(map(int, input().split()))

l = [list(map(int, input().split())) for _ in range(N)]

l.sort(key=lambda x: (x[1], x[2], x[3], x[0]!=M))

for i in range(N):
    if l[i][0]==M:
        print(i+1)
        break
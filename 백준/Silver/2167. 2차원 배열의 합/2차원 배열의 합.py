import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))




for _ in range(int(input())):
    i, j, x, y = list(map(int, input().split()))
    answer = 0
    for q in range(i-1,x):
        answer += sum(l[q][j-1:y])
    print(answer)
    
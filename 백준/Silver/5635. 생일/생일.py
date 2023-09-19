import sys
input = sys.stdin.readline


n = int(input())

l = [list(input().split()) for _ in range(n)]

l.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1]), x[0]))



print(l[-1][0])
print(l[0][0])

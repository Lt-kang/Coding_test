import sys
input = sys.stdin.readline


N = int(input())
A, B = list(map(int, input().split()))
C = int(input())
l = [int(input()) for _ in range(N)]
l.sort(reverse=True)

answer = []

for i in range(N+1):
    answer.append(((C+sum(l[:i]))//(A+(B*(i)))))
    
print(max(answer))

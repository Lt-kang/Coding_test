import sys
input = sys.stdin.readline



n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = a+b
answer.sort()
for i in range(len(answer)):
    print(answer[i],end=' ')
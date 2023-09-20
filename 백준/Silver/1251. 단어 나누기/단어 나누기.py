import sys
# input = sys.stdin.readline


w = input()

answer = []
for i in range(1,len(w)-1):
    for j in range(i+1,len(w)):
        a = w[:i]
        b = w[i:j]
        c = w[j:]
        answer.append(a[::-1] + b[::-1] + c[::-1])

answer.sort()
print(answer[0])
import sys
input = sys.stdin.readline


n, m = list(map(int, input().split()))

l = []
for _ in range(n):
    l.append(int(input()))

l.sort()


answer = int(2e9)

s=0
e=0
while s<=e and e<n:
    temp = l[e]-l[s]
    if temp < m:
        e += 1
    else:
        answer = min(answer, temp)
        s += 1

print(answer)

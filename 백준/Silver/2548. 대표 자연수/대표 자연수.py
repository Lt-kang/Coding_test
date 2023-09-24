import sys
input = sys.stdin.readline


n = int(input())
l = list(map(int, input().split()))
l.sort()

mid = len(l)//2
detect = range(mid-1,mid+1)

answer = []
for i in detect:
    temp = []
    for j in range(n):
        temp.append(abs(l[j]-l[i]))

    answer.append([l[i], sum(temp)])

answer.sort(key=lambda x: (x[1], x[0]))
print(answer[0][0])

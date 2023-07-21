import sys; input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

pre_sum = [0]
temp = 0
for i in l:
    temp += i
    pre_sum.append(temp)

for _ in range(m):
    s, e = map(int,input().split())
    print(pre_sum[e] - pre_sum[s-1])
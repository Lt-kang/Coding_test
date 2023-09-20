import sys
input = sys.stdin.readline


t = int(input())
l = [int(input()) for _ in range(t)]
l.sort(reverse=True)


mx = -1
for i in range(t-2):
    if l[i] < sum(l[i+1:i+3]):
        mx = max(mx, sum(l[i:i+3]))
print(mx)
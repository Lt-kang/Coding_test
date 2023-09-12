import sys
input = sys.stdin.readline


l = [int(input()) for _ in range(5)]
l.sort()
print(sum(l)//len(l))

s = 0
e = len(l)
mid = (s+e)//2

if len(l)%2==0:
    print((l[mid]+l[mid-1])//2)
else:
    print(l[mid])


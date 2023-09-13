import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()

s = 0
e = n-1
mn = abs(l[s] + l[e])
idx = [s, e]

while s<e:
    t = l[s]+l[e]

    if abs(t) < mn:
        mn = abs(t)
        idx = [s, e]
        if t==0: break
    
    if t<0: s += 1
    else: e -= 1
    

print(f"{l[idx[0]]} {l[idx[1]]}")
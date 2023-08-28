n = int(input())
l = list(map(int, input().split()))
x = int(input())


l.sort()

s = 0
e = len(l)-1


cnt = 0
while s<e:
    if l[s]+l[e]==x: 
        cnt += 1

    if l[s]+l[e]>x: e -=1
    else:
        s += 1

print(cnt)
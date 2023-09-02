n, m = list(map(int, input().split()))
l = list(map(int, input().split()))

s = 0
e = 1

cnt = 0
while e <= n and s<=e:
    s_l = sum(l[s:e])
    if s_l==m: 
        cnt += 1
        e += 1
    elif s_l<m: e += 1
    elif s_l>m: s += 1

print(cnt)
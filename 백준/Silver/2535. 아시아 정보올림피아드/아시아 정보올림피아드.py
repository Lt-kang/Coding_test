n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]
l.sort(reverse=True, key= lambda x : x[2])



print(f"{l[0][0]} {l[0][1]}")
idx = 1
temp = [l[0][0]]
while len(temp)!=3:
    if temp.count(l[idx][0]) < 2:
        print(f"{l[idx][0]} {l[idx][1]}")
        temp.append(l[idx][0])
        idx += 1
    else:
        idx += 1



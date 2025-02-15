N = int(input())
M = int(input())
_list = sorted(list(map(int, input().split())))

s = 0
e = N-1
cnt = 0
while s != e:
    temp_num = _list[s] + _list[e]
    if temp_num == M:
        cnt += 1
        s += 1

    elif temp_num > M:
        e -= 1

    elif temp_num < M:
        s += 1 


print(cnt)


K, N = map(int, input().split())
_list = [int(input()) for _ in range(K)]


start, end = 1, max(_list)
while start <= end:
    mid = (start + end)//2

    cnt = 0
    for line in _list:
        cnt += line//mid

    if cnt >= N:
        start = mid+1
    else:
        end = mid-1

# print("========================")
print(start-1)

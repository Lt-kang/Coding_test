n = int(input())
l = list(map(int, input().split()))

_dict = dict()

for i in range(n):
    _dict[l[i]] = 0


m = int(input())
t = list(map(int, input().split()))

for j in range(m):
    if t[j] not in _dict:
        print(0, end=' ')
    else:
        print(1, end=' ')
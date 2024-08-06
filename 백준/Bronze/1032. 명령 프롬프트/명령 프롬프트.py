import sys
input = sys.stdin.readline


t = int(input())

_list = [input() for _ in range(t)]

for r in range(len(_list[0])):
    _temp = []
    for c in range(t):
        _temp.append(_list[c][r])

    if len(set(_temp))==1:
        print(_temp[0], end='')
    else:
        print("?", end='')
from collections import deque


N = int(input())
_deque = deque(range(1, N+1))
_balloon = list(map(int, input().split()))

_map = {d:b for d, b in zip(_deque, _balloon)}

answer = []
while _deque:
    _temp = _deque[0]
    answer.append(str(_temp))
    _deque.remove(_temp)
    rot_cnt = _map[_temp]
    if rot_cnt > 0:
        _deque.rotate(-(_map[_temp]-1))
    elif rot_cnt < 0:
        _deque.rotate(-_map[_temp])

        

print(' '.join(answer))
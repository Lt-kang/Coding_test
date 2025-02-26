from collections import deque

N, M = map(int, input().split())
target_elements = list(map(int, input().split()))

_deque = deque(range(1, N + 1))
cnt = 0
for target in target_elements:
    _idx = _deque.index(target)

    if _idx == 0:
        _deque.popleft()
        continue
    
    
    minus_rot = len(_deque) - _idx
    if _idx > minus_rot:
        _deque.rotate(minus_rot)
        cnt += minus_rot

    else:
        _deque.rotate(-_idx)
        cnt += _idx

    _deque.popleft()
    

print(cnt)






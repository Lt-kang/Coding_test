from collections import deque
def solution(n_str):
    l = len(n_str)
    n_str = deque(n_str)
    for i in range(l):
        temp = n_str.popleft()
        if temp=="0": pass
        else: n_str.appendleft(temp); break
    return ''.join(list(n_str))
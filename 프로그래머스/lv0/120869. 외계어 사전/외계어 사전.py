from collections import deque

def solution(s, d):
    d = deque(d)
    for w in s:
        for _ in range(len(d)):
            t = d.popleft()
            if w in t:
                d.append(t)

    return 1 if d else 2
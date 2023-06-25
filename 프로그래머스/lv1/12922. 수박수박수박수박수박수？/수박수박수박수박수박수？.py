from collections import deque
def solution(n):
    w = deque(["수","박"])
    answer = ""
    for i in range(n):
        answer += w[0]
        w.append(w.popleft())
    return answer
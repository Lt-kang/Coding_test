from collections import deque
def solution(p, s):
    answer = []
    s = deque(s)
    while p:
        p = deque([p[i]+s[i] for i in range(len(s))])
        cnt = 0
        while p:
            if p[0]>=100:
                p.popleft()
                s.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)
    return [i for i in answer if i!=0]
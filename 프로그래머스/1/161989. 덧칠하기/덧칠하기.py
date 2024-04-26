from collections import deque
def solution(n, m, section):
    section = deque(section)

    cnt = 0
    while section:
        cnt += 1
        p_range = section[0] + (m-1)
        for _ in range(m):
            if section and section[0] <= p_range:
                section.popleft()
            
                 
    return cnt
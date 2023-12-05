from collections import deque
def solution(s):
    list_s = list(s)
    s = deque(list(s))

    temp = deque()
    answer = []
    
    for w in list_s:
        if w not in temp:
            answer.append(-1)
        else:
            answer.append(temp.index(w)+1)

        temp.appendleft(s.popleft())
    

    return answer
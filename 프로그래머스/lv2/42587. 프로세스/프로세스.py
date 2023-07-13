from collections import deque
def solution(p, l):
    p = deque(p)
    answer = 0
    while p:
        if p[0]==max(p) and l==0: answer +=1; break
        elif p[0]==max(p): 
            answer += 1; 
            p.popleft(); 
            l-=1; 
            if l==-1: l += len(p)
        else:
            p.rotate(-1);
            l -= 1
            if l==-1: l += len(p)
    return answer
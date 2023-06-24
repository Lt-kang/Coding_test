from collections import deque
def solution(s):
    if s[0]==")": return False
    
    s = deque(list(s))
    temp = 0
    for i in range(len(s)):
        s_left = s.popleft()
        if temp < 0: return False
        if s_left=="(": temp += 1
        elif s_left==")": temp -= 1
        
    if temp != 0: return False
    else: return True
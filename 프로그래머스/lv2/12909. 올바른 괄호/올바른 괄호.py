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

# 개선 코드
def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0: break  
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
        # x=="("면 pair + 1 그 반대면 pair -1
        # 중간에 pair가 음수가 되면 잘못된 괄호 이므로 반복문 종료 이때 반복문 종료시 pair != 0 이므로 return 값은 자연스럽게 False가 됨.
    return pair == 0
        # pair가 0인 경우 = 괄호가 정상인 경우 = True / 그 외에는 전부 False로 출력
    

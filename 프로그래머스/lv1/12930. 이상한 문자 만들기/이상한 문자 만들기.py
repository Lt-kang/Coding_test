def trans_word(s):
    return ''.join([w.upper() if idx%2==0 else w.lower() for idx, w in enumerate(s)])
    
def solution(s):
    s = s.split(" ")
    answer = ""
    for i in range(len(s)):
        answer += trans_word(s[i])
        answer += " "
    return answer[:-1]
    
    
def solution(s):
    switch = 0
    s = list(s.lower())
    s[0] = s[0].upper()
    
    for idx, w in enumerate(s):
        if switch==1 and w!=" ": s[idx] = w.upper(); switch = 0
        if w==" ": switch = 1
    return ''.join(s)
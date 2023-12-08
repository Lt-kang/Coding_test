def solution(code):
    mode = 0
    ret = ""
    
    for idx, w in enumerate(code):
        if mode == 0:
            if w == "1": mode = 1
            else:
                if idx%2==0: ret += w

        elif mode == 1:
            if w == "1": mode = 0
            else:
                if idx%2!=0: ret += w
        
        
    return ret if ret else "EMPTY"
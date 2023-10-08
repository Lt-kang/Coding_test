def solution(s):
    l = s.index("l") if "l" in s else 21
    r = s.index("r") if "r" in s else 21
    
    if l < r:
        return s[:l] 
    elif l > r:
        return s[r+1:]
    elif l==r==21:
        return []
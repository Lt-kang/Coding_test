def solution(strArr):
    l = len(strArr)
    for i in range(l-1,-1,-1):
        if "ad" in strArr[i]: del strArr[i]
    return strArr
def solution(myString, pat):
    return 1 if pat.replace("A","a").replace("B","b") in myString.replace("A","b").replace("B","a") else 0
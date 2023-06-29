def solution(numLog):
    answer = ""
    l = len(numLog)
    for i in range(1,l):
        t = numLog[i]-numLog[i-1]
        if t == 1: answer += "w"
        elif t == -1: answer += "s"
        elif t == 10: answer += "d"
        elif t == -10: answer += "a"
    return answer
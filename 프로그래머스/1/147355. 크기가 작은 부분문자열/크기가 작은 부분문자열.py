def solution(t, p):
    tLen = len(t)
    pLen = len(p)
    cnt = 0

    for i in range(tLen + 1 - pLen):
        if int(t[i:i+pLen]) <= int(p):
            cnt += 1

    return cnt
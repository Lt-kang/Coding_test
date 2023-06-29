def solution(intStrs, k, s, l):
    return [int(w[s:s+l]) for w in intStrs if int(w[s:s+l])>k]
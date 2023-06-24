def solution(s):
    s = list(s.split(" "))
    s = [int(i) for i in s]
    mx = max(s)
    mn = min(s)
    return str(mn) + " " + str(mx)
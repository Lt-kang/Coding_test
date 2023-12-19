def solution(a, q):
    for idx, i in enumerate(q):
        if idx%2==0:
            a = a[:i + 1]
        else:
            a = a[i:]

    return a



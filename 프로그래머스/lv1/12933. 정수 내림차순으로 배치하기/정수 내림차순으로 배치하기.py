def solution(n):
    n = list(str(n))
    n = list(map(int, n))
    n.sort(reverse=True)
    n = list(map(str, n))
    n = int(''.join(n))
    return n
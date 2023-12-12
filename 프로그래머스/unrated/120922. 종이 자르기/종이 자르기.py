def solution(M, N):
    mn = min(M, N)
    mx = max(M, N)

    return (mn - 1) + mn * (mx-1)
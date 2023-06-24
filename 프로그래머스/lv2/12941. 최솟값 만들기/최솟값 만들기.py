def solution(A,B):
    l = len(A)
    A = sorted(A)
    B = sorted(B, reverse=True)
    return sum([A[i]*B[i] for i in range(l)])
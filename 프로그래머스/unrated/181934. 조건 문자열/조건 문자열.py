def solution(ineq, eq, n, m):
    return 1 if eval((str(n)+ineq+eq+str(m)).replace("!","")) else 0
def grad(p1, p2):
    return (p2[1] - p1[1])/(p2[0] - p1[0])

def solution(dots):
    p1, p2, p3, p4 = dots

    cond1 = grad(p1, p2) == grad(p3, p4)
    cond2 = grad(p1, p3) == grad(p2, p4)
    cond3 = grad(p1, p4) == grad(p2, p3)

    if cond1 or cond2 or cond3: return 1
    
    return 0
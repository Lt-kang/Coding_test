def solution(brown, yellow):
    ab = brown + yellow
    for b in range(1, ab+1):
        if (ab / b) % 1 == 0: # 정수일 경우
            a = ab/ b 
            if (a >= b) and (a*2 + b*2 == brown + 4):
                return [a,b]
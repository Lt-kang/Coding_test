def solution(p, k):
    answer = []

    for line in p:
        temp = [s*k for s in line]
        for _ in range(k):
            answer.append(''.join(temp))
            
    return answer


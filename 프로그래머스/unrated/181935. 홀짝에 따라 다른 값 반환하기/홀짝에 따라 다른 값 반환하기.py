def solution(n):
    if n%2==0:
        answer = sum([i**2 for i in range(n,0,-2)])
    else: 
        answer = sum([i for i in range(n,0,-2)])
    return answer
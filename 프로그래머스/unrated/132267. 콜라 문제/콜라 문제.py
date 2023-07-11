def solution(a, b, n):
    answer = 0
    while True:
        t = n%a
        n = (n//a)*b
        answer += n
        n += t

        if n < a: return answer
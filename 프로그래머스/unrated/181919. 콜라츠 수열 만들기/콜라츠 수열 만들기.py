def collatz(num):
    if num%2==0: return num//2
    else: return 3*num+1
def solution(n):
    answer = [n]
    while True:
        n = collatz(n)
        answer.append(n)
        if n==1: break
    return answer



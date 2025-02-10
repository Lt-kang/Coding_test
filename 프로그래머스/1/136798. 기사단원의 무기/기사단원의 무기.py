def divisor_cnt(number):
    if number == 1: return 1
    cnt = 0
    for i in range(1, 1+int(number**0.5)):
        cnt += 1 if number%i==0 else 0
    
    cnt *= 2
    if int(number**0.5)==number**0.5 and number%int(number**0.5)==0: cnt -= 1
    return cnt
    

def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        divisor = divisor_cnt(i)
        answer += power if divisor > limit else divisor

    return answer
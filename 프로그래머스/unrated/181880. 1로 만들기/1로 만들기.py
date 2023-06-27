def trans_one(num):
    cnt = 0
    if num==1: return 0
    while True:
        cnt += 1
        if num%2==0: num //= 2
        elif num%2!=0: num = (num-1)//2
        
        if num==1: 
            return cnt
        
def solution(num_list):
    return sum([trans_one(i) for i in num_list])
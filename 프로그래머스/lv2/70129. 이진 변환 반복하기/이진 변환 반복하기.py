def func1(num):
    zero_count = num.count("0")
    num = len(num.replace("0",""))
    return bin(num)[2:], zero_count

def solution(s):
    if s=="1": return [0,0]

    zero_count = []
    cnt = 0
    
    while True:
        s,b = func1(s)
        cnt += 1
        zero_count.append(b)
        if s=="1": break
    return [cnt, sum(zero_count)]
def solution(num, total):
    if num%2!=0:
        x = total//num
        a = [x+i for i in range(1, num//2+1)]
        b = [x-i for i in range(1, num//2+1)]
        return sorted(a+[x]+b)
    elif num%2==0:
        x = (total-num//2)//num
        a = [x+i for i in range(1, num//2+1)]
        b = [x-i for i in range(1, num//2)]
        return sorted(a+[x]+b)
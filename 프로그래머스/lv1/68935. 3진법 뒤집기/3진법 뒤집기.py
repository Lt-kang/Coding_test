def decimal_to_ternary(decimal_num):
    if decimal_num == 0:
        return '0'
    
    ternary_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 3
        ternary_num = str(remainder) + ternary_num
        decimal_num = decimal_num // 3
    
    return ternary_num

def solution(n):
    return int(str(decimal_to_ternary(n))[::-1],3)
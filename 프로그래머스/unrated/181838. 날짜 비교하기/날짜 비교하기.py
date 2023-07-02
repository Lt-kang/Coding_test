def solution(date1, date2):
    return 1 if sum([(date2[i]-date1[i])*10**(3-i) for i in range(3)])>0 else 0
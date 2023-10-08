def solution(r, a):
    l = list(zip(r,a))
    l.sort(key=lambda x:(x[1]!=True, x[0]))
    print(l)
    answer = 0
    for i in range(3):
        if l[i][1]: answer += r.index(l[i][0])*10000/100**i
            
    return answer
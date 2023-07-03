def solution(sides):
    return len(list(range(max(sides)-min(sides)+1,max(sides)+1))+list(range(max(sides)+1,sum(sides))))
    
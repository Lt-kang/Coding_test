def solution(k, m, score):
    score.sort(reverse=True)
    return sum([score[i]*m for i in range(len(score)) if (i+1)%m==0])


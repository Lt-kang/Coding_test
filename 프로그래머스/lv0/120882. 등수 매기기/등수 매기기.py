def solution(score):
    score_mean = [(s[0]+s[1])/2 for s in score]
    score_mean.sort(reverse=True)
    answer = [score_mean.index((s[0]+s[1])/2)+1 for s in score]
    
    return answer
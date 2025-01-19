def solution(k, score):
    answer = []
    temp_list = []
    for s in score:
        temp_list.append(s)
        temp_list.sort(reverse=True)
        
        
        if len(temp_list) <= k:
            answer.append(temp_list[-1])
        else:
            answer.append(temp_list[k-1])
        
    return answer
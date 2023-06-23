def solution(num_list, n):
    cnt = 0
    answer = []
    while True:
        if 0+n*cnt<len(num_list): answer.append(num_list[0+n*cnt]); cnt+=1
        else: break
    return answer
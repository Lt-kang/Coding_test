def solution(array):
    if len(set(array))==1: return array[0]
    answer = [[array.count(i),i] for i in set(array)]
    answer.sort(reverse=True)
    if answer[0][0]==answer[1][0]: return -1
    else: return answer[0][1]
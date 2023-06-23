def solution(num_list, n):
    cnt = 0
    answer = []
    while True:
        if 0+n*cnt<len(num_list): answer.append(num_list[0+n*cnt]); cnt+=1
        else: break
    return answer

###########################
# 더 깔끔한 코드
# Slicing을 잘 활용하자.
def solution(num_list, n):
    return num_list[::n]

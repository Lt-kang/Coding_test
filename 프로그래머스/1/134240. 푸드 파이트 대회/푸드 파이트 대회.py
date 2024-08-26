def solution(food):
    answer = ''.join([str(idx+1)*(i//2) for idx, i in enumerate(food[1:])])
    return answer + "0" + ''.join(list(reversed(answer)))
from itertools import combinations
def solution(arr):
    answer = []
    for i in combinations(arr, 2):
        answer.append(sum(i))

    answer = sorted(list(set(answer)))
    return answer
from collections import deque
def solution(arr):
    l = len(arr)
    point = 0
    answer = [arr[0]]
    arr = deque(arr)
    for i in range(l):
        temp = arr.popleft()
        if temp==answer[point]: pass
        else: answer.append(temp); point += 1
    return answer
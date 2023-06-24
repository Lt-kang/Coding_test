from collections import deque
def solution(arr, delete_list):
    l = len(arr)
    arr = deque(arr)
    for i in range(l):
        if arr[0] in delete_list:
            arr.popleft()
        else: arr.append(arr.popleft())
    return list(arr)
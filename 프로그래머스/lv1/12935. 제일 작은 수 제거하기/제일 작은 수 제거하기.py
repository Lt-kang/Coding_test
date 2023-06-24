from collections import deque
def solution(arr):
    mn = min(arr)
    l = len(arr)
    if l==1: return [-1]
    
    arr = deque(arr)
    check = 0
    for i in range(l):
        if arr[0]==mn: arr.popleft()
        else: arr.append(arr.popleft())
    return list(arr)
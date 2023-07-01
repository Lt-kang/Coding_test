def solution(arr):
    l = [2**i for i in range(10+1) if 2**i>=len(arr)]
    if l[0]==len(arr): answer = arr
    else:
        answer = arr + [0]*(l[0]-len(arr))
    return answer
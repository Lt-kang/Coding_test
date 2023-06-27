def solution(arr, idx):
    try:
        answer = arr[idx:].index(1)+idx
    except:
        return -1
    return answer
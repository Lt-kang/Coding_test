def solution(arr, n):
    odd = [i+n if (idx+1)%2!=0 else i for idx, i in enumerate(arr)]
    even = [i+n if (idx+1)%2==0 else i for idx, i in enumerate(arr)]
    return odd if len(arr)%2!=0 else even
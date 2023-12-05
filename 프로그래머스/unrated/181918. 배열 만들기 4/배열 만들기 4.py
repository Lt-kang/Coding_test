def solution(arr):
    stk = []
    idx = 0

    while idx < len(arr):
        if stk and arr[idx] <= stk[-1]:
            stk.pop()
        else:
            stk.append(arr[idx])
            idx += 1

    return stk
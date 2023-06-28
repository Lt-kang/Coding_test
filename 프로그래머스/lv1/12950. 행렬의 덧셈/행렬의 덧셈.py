def solution(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr1[0])
    return [[arr1[j][i]+arr2[j][i] for i in range(l2)] for j in range(l1)]
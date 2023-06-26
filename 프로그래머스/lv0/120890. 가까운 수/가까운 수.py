def solution(array, n):
    array.append(n)
    array.sort()
    if array[-1] == n: return array[-2]
    if array[0] == n: return array[1]
    idx = array.index(n)
    return array[idx+1] if abs(array[idx]-array[idx+1]) < abs(array[idx]-array[idx-1]) else array[idx-1]
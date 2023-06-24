def lcm(A, B):
    for i in range(max(A,B), (A*B) + 1):
	    if i % A == 0 and i % B == 0: return i
def solution(arr):
    for i in range(1,len(arr)):
        arr[i] = lcm(arr[i-1],arr[i])
    return arr[-1]
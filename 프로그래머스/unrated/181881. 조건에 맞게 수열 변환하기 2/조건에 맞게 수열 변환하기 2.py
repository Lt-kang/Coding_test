def func(num):
    if 50<=num and num%2==0: return num//2
    elif 50>num and num%2!=0: return num*2 +1
    else: return num

def solution(arr):
    cnt = 0
    while True:
        arr1 = arr[:]
        arr = [func(i) for i in arr]
                
        if arr1 == arr: return cnt
        else: cnt += 1
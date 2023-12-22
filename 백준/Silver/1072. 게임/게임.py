import sys

x, y = map(int, input().split())

s = 0
e = x

target = (y * 100 // x)
if target > 98:
    print(-1)

else:
    answer = sys.maxsize
    while s <= e:
        
        mid = (s + e)//2
        temp = (y + mid) * 100 // (x + mid)
        
        if temp > target:
            answer = min(mid, answer)
            e = mid - 1
        else:
            s = mid + 1
            
    

    print(answer)
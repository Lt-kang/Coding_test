import sys
input = sys.stdin.readline


def binary(num):
    s = 0
    e = num
    while s<=e:
        mid = (s+e)//2
        if mid**2 == num:
            return mid
        else:
            if mid**2 > num:
                e = mid -1
            elif mid**2 < num:
                s = mid + 1


print(binary(int(input())))

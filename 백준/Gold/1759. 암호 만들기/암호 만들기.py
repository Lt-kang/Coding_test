import sys
import itertools

def check(str):
    temp = list(str)
    cnt = 0
    check_list = ['a','e','i','o','u']
    for i in check_list:
        t = temp.count(i)
        cnt += t
    
    if cnt>=1 and len(str)-2 >= cnt:
        return True
    else: return False

m, t = map(int, sys.stdin.readline().split())

n = list(map(str, sys.stdin.readline().split()))

n.sort()

p = list(itertools.combinations(n,m))

for value in p:
    if check(value):
        print(''.join(map(str, value)))


# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 
# 최소 한 개의 모음(a, e, i, o, u)과 
# 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.

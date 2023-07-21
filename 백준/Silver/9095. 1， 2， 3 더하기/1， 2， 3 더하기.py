from itertools import product

n = int(input())
num = [1,2,3]

for _ in range(n):
    cnt = 0
    t = int(input())
    for i in range(1,1+t):
        for w in product(num,repeat=i):
            if sum(w)==t: cnt += 1

    print(cnt)
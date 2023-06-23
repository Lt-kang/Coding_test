import sys
import itertools

n, s = map(int, sys.stdin.readline().split())

t = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(len(t)):
    p = list(itertools.combinations(t,i+1))
    for j in p:
        if sum(list(j)) == s :
            cnt += 1

print(cnt)

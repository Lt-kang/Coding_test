from math import gcd
import itertools


t = int(input())


for _ in range(t):
    n = list(map(int, input().split()))
    l = n[1:]
    n = n[:1]
    answer = []
    for i in itertools.combinations(l,2):
        answer.append(gcd(i[0], i[1]))

    print(sum(answer))






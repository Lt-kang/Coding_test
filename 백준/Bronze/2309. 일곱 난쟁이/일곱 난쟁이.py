from itertools import combinations
import sys
input = sys.stdin.readline


l = [int(input()) for _ in range(9)]

combi = combinations(l, 7)

for table in combi:
    if sum(table)== 100:
        answer = list(table)
        break

answer.sort()
for i in answer:
    print(i)


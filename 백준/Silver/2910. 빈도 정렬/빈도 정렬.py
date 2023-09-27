from collections import Counter
import sys; input = sys.stdin.readline


N, C = list(map(int, input().split()))
l = list(map(int, input().split()))
l_counter = Counter(l)
l_keys = l_counter.keys()
l_values = l_counter.values()

answer = l[:]
answer.sort(reverse=True, key= lambda x : (l_counter[x], -l.index(x)))
for i in answer:
    print(i, end=' ')
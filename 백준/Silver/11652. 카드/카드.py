from collections import Counter
import sys
input = sys.stdin.readline



n = int(input())
l = [int(input()) for _ in range(n)]

count_dict = Counter(l)
def key_func(x):
    return (-count_dict[x], x)


l.sort(key=key_func)

print(l[0])

import sys
input = sys.stdin.readline


T = int(input())
l = [list(input().split()) for _ in range(T)]

increasing = sorted(l)
decreasing = sorted(l, reverse=True)

if l==increasing:
    print("INCREASING")
elif l==decreasing:
    print("DECREASING")
else:
    print("NEITHER")

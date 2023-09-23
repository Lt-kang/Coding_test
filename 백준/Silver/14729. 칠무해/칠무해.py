import sys
input = sys.stdin.readline


T = int(input())
l = [float(input()) for _ in range(T)]
l.sort()

for i in range(7):
    print("%.3f" %l[i])
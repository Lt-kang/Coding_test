import sys
input = sys.stdin.readline
for i in sorted([int(input()) for _ in range(int(input()))],reverse=True):
    print(i)

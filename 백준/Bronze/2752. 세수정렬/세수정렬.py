import sys
input = sys.stdin.readline


l = list(map(int, input().split()))
l.sort()
print(' '.join([str(i) for i in l]))



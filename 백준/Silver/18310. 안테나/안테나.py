import sys
input = sys.stdin.readline


n = int(input())
l = list(map(int, input().split()))
l.sort()

mid = len(l)//2 if len(l)%2!=0 else (len(l)//2)-1
print(l[mid])
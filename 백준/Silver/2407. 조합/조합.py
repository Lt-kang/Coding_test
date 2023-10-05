import sys; input = sys.stdin.readline
import math

n, m = list(map(int, input().split()))

print(math.comb(n, m))
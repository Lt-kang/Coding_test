import sys
input = sys.stdin.readline


N, M = map(int, input().strip().split())

_map = {}
for _ in range(N):
    k, v = input().strip().split()
    _map[k] = v

for _ in range(M):
    print(_map[input().strip()])
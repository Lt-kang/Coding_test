import sys
input = sys.stdin.readline

from collections import defaultdict

_map = defaultdict(bool)

n = int(input().rstrip())

for _ in range(n):
    person, state = input().rstrip().split()
    _map[person] = True if state == 'enter' else False

for name in sorted([k for k, v in _map.items() if v is True], reverse=True):
    print(name)






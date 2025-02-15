import sys
input = sys.stdin.readline


N, M = map(int, input().strip().split())

_dict1 = {str(i+1):input().strip() for i in range(N)}
_dict2 = {v:k for k, v in _dict1.items()}

for _ in range(M):
    q = input().strip()
    if q.isnumeric():
        print(_dict1[q])
    else:
        print(_dict2[q])
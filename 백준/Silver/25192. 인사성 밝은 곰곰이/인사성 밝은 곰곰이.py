from collections import defaultdict
import sys
input = sys.stdin.readline


_dict = defaultdict()
cnt = 0
for i in range(int(input().strip())):
    _command = input().strip()
    if _command == 'ENTER':
        cnt += len(_dict.keys())
        _dict = defaultdict()
    else:
        _dict[_command] = True

cnt += len(_dict.keys())
print(cnt)




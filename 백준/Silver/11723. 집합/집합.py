import sys
input = sys.stdin.readline        


n = int(input().strip())

_set = set()
for _ in range(n):
    command = input().strip().split()
    c = command[0]

    if c == 'add':
        _set.add(int(command[1]))

    elif c == 'check':
        print(1 if int(command[1]) in _set else 0)

    elif c == 'remove':
        _set.discard(int(command[1]))

    elif c == 'toggle':
        n = int(command[1])
        if n in _set:
            _set.discard(n)
        else:
            _set.add(n)

    elif c == 'all':
        _set = set(range(1, 20+1))

    elif c == 'empty':
        _set = set()

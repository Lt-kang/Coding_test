import sys
input = sys.stdin.readline


_set = set(['ChongChong'])
for i in range(int(input().strip())):
    A, B = input().strip().split()

    if A in _set:
        _set.add(B)

    if B in _set:
        _set.add(A)

print(len(_set))




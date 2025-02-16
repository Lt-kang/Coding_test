

A = list(input())
_set = set()
for i in range(len(A)):
    for j in range(i, len(A)):
        _set.add(''.join(A[i:j+1]))

print(len(_set))
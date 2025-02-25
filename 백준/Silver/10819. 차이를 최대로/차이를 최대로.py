from itertools import permutations

N = int(input())
_elements = list(map(int, input().split()))

_max = 0
for table in permutations(_elements, N):
    
    _temp = 0
    for i in range(len(table)-1):
        _temp += abs(table[i] - table[i+1])

    _max = max(_max, _temp)

print(_max)



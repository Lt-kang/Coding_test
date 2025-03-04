from itertools import product

N = int(input())

_sorted_list = sorted([''.join(list(map(str, table))) for table in product([0, 1], repeat=N)], key= lambda x: (x.count('1'), ''.join(reversed(x))))

target = input()
print(_sorted_list.index(target))

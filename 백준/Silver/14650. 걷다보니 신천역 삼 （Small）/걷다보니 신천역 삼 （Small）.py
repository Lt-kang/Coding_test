from itertools import product

_elements = [0, 1, 2]

N = int(input())

cnt = 0
for table in product(_elements, repeat=N-1):
    num = ''.join(map(str, table))

    cnt += 1 if int(f'1{num}') % 3 == 0 else 0
    cnt += 1 if int(f'2{num}') % 3 == 0 else 0

print(cnt)
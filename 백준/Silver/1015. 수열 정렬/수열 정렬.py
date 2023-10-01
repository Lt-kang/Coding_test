import sys
input = sys.stdin.readline


n = int(input())
l = list(map(int, input().split()))

l_sort = sorted(l[:])


temp = []
for i in l:
    if i in temp:
        print(l_sort.index(i)+temp.count(i),end=' ')
        temp.append(i)
    else:
        print(l_sort.index(i), end=' ')
        temp.append(i)

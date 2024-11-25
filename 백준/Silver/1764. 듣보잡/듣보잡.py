import sys
input = sys.stdin.readline


N, M = map(int, input().split())

list1 = set([input().strip() for _ in range(N)])
list2 = set([input().strip() for _ in range(M)])


print(len(list1 & list2))
for i in sorted(list1 & list2):
    print(i)

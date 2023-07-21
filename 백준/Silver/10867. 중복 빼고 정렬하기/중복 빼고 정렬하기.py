n = int(input())
l = sorted(list(set(map(int, input().split()))))
print(' '.join([str(w) for w in l]))
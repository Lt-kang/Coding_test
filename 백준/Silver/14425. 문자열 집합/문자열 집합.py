import sys; input = sys.stdin.readline


n, m = map(int, input().split())

l_n = [input() for _ in range(n)]
l_m = [input() for _ in range(m)]


cnt = 0
for w in l_m:
    if w in l_n:
        cnt += 1

print(cnt)
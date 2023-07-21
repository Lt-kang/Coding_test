import sys; input = sys.stdin.readline

N = int(input())

n_d = dict()
for i in list(map(int, input().split())):
    if str(i) not in n_d: n_d[str(i)] = 1
    else: n_d[str(i)] += 1
     

M = int(input())
answer = [str(n_d[str(i)]) if str(i) in n_d else "0" for i in list(map(int, input().split()))]

print(" ".join(answer))
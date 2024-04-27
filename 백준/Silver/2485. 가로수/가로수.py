import math

N = int(input())
list_ = [int(input()) for _ in range(N)]
list_compare = [list_[i+1] - list_[i] for i in range(N-1)]
gcd_ = list_compare[0]

for i in range(1, len(list_compare)):
    gcd_ = math.gcd(gcd_, list_compare[i])


cnt = 0
for j in list_compare:
    cnt += (j // gcd_) - 1

print(cnt)
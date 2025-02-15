n = int(input())
_list = list(map(int, input().split()))
T, P = map(int, input().split())

t_cnt = 0
for i in _list:
    if i == 0: continue
    t_cnt += (i//T) if i%T==0 else (i//T) + 1


print(t_cnt)
print(f"{n//P} {n%P}")


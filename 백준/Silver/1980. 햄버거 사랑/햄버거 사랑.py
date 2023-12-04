n, m, t = map(int, input().split())


mx = max(n, m)
mn = min(n, m)

cnt = 0

count = 0
coke = 10000

while t >= mx*cnt:
    temp_t = t
    temp_count = cnt
    temp_coke = 0

    temp_t -= mx*cnt
    temp_count += temp_t//mn
    temp_coke += temp_t%mn

    if coke > temp_coke:
        count = temp_count
        coke = temp_coke
    elif coke == temp_coke and count < temp_count:
        count = temp_count
        coke = temp_coke

    cnt += 1
    

    

print(f"{count} {coke}")





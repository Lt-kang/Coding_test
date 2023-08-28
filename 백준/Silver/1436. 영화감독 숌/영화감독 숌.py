n = int(input())

start = 666

cnt = 1
while True:
    if cnt == n: break
    else:
        start += 1
    if '666' in str(start): cnt += 1
    
print(start)
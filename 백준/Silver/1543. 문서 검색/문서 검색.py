
w = input()
answer = input()

s = 0
e = len(answer)

cnt = 0
while e<=len(w):
    if ''.join(w[s:e])==answer:
        cnt += 1
        s += len(answer)
        e += len(answer)
    else:
        s += 1
        e += 1

print(cnt)
        

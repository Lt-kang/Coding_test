# ord('A') = 65
# -55

n, b = list(map(int, input().split()))

answer = []
while n!=0:
    t = n%b
    if t>=10: t = chr(t+55)
    answer.append(str(t))
    n //= b

answer = answer[::-1]
print(''.join(answer))

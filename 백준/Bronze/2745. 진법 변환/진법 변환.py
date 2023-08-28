# ord('A') = 65
# -55

n, b = list(input().split())

b = int(b)
n = n[::-1]
# print(n)

answer = 0
for idx, w in enumerate(n):
    if ord(w) >= 65:
        answer += (ord(w)-55)*b**idx
    else:
        answer += int(w)*b**idx

print(answer)

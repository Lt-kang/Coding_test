
# ord("a") = 97

t = int(input())
a = input()
b = []
rt = 0

for i in a:
    b.append(ord(i)-96)

for k in range(t):
    rt += b[k]*(31**k)

print(rt)
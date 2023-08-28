l = list(map(int, input().split()))

a = l[0]
b = l[1]
c = l[2]
d = l[3]
e = l[4]
f = l[5]

for x in range(-999,1000,1):
    for y in range(-999,1000,1):
        if ((a*x)+(b*y)==c) and ((d*x)+(e*y)==f):
            print(f"{x} {y}")
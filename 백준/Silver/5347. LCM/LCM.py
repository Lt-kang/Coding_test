from math import lcm

for _ in range(int(input())):
    t = list(map(int, input().split()))
    print(lcm(t[0],t[1]))

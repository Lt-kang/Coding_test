import sys
input = sys.stdin.readline


while True:
    t = int(input())
    if t == 0: break

    print(sum(range(t+1)))




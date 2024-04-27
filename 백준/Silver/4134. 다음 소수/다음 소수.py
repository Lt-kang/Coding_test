import sys
input = sys.stdin.readline
N = int(input())

def prime(x):
    for i in range(2, 1+int(x**0.5)):
        if x%i==0: return False
    return True

for _ in range(N):
    n = int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if prime(n):
            print(n)
            break
        else:
            n += 1
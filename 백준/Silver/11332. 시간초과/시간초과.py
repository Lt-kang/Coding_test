import sys; input = sys.stdin.readline
import math

def time_out(time, num):
    print("May Pass." if time*10**8 >= num else "TLE!")
C = int(input())

for _ in range(C):
    S, N, T, L = list(input().split())
    
    if S == "O(N)": time_out(int(L), int(N)*int(T))
    elif S == "O(N^2)": time_out(int(L), (int(N)**2)*int(T))
    elif S == "O(N^3)": time_out(int(L), (int(N)**3)*int(T))
    elif S == "O(2^N)": time_out(int(L), (2**int(N))*int(T))
    elif S == "O(N!)": time_out(int(L), math.factorial(int(N))*int(T))




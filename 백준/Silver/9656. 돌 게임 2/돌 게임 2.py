import sys
input = sys.stdin.readline



n = int(input().strip())

print("SK" if n % 2 == 0 else "CY")

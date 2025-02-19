import sys

input = sys.stdin.readline
n = int(input().strip())

cnt = 0
max_stick = 0

stick_list = [int(input().strip()) for _ in range(n)]
for stick in reversed(stick_list):
    if stick > max_stick:
        cnt += 1
        max_stick = stick

print(cnt)

    
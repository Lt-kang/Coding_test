import sys
input = sys.stdin.readline

from collections import deque

deq = deque()

# print("=============")


n = int(input().rstrip())

for _ in range(n):
    command = input().rstrip().split()

    if command[0] == '1':
        deq.appendleft(int(command[1]))

    elif command[0] == '2':
        deq.append(int(command[1]))

    elif command[0] == '3':
        print(-1 if not deq else deq.popleft())

    elif command[0] == '4':
        print(-1 if not deq else deq.pop())

    elif command[0] == '5':
        print(len(deq))

    elif command[0] == '6':
        print(1 if not deq else 0)

    elif command[0] == '7':
        print(-1 if not deq else deq[0])

    elif command[0] == '8':
        print(-1 if not deq else deq[-1])


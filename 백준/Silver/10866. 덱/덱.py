from collections import deque
import sys

temp = deque()

for i in range(int(sys.stdin.readline())):

    n = list(sys.stdin.readline().split())

    if n[0]=="push_front":
        temp.appendleft(int(n[1]))

    elif n[0]=="push_back":
        temp.append(int(n[1]))

    elif n[0]=="pop_front": 
        if len(temp) == 0:
            print(-1)
        else:
            print(temp.popleft())

    elif n[0]=="pop_back": 
        if len(temp) == 0:
            print(-1)
        else:
            print(temp.pop())

    elif n[0]=="size":
        print(len(temp))

    elif n[0]=="empty":
        if len(temp) == 0:
            print(1)
        else:
            print(0)

    elif n[0]=="front":
        if len(temp) == 0:
            print(-1)
        else:
            print(temp[0])

    elif n[0]=="back": 
        if len(temp) == 0:
            print(-1)
        else:
            print(temp[-1])
n = int(input())

origin_list = list(range(1, n+1))
temp_stack = []
answer = []
sw = True
for _ in range(n):
    c = int(input())

    while True:
        if not temp_stack or temp_stack[-1] != c:
            answer.append("+")
            if origin_list:
                temp_stack.append(origin_list.pop(0))
            elif not origin_list:
                sw =  False
                break

        elif temp_stack[-1] == c:
            answer.append("-")
            temp_stack.pop()
            break



if sw:
    for c in answer:
        print(c)

else:
    print("NO")


    


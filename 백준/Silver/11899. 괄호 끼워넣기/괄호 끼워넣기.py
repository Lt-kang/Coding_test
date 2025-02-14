pipe = input()


stack = []
answer = 0
for p in pipe:
    if p == ')':
        if not stack or stack[-1] == ')':
            answer += 1
        elif stack[-1] == '(':
            stack.pop()


    elif p == '(':
        stack.append(p)


print(answer + len(stack))

N = int(input())

students = list(map(int, input().split())) 
stack = []

cnt = 1
for s in students:
    stack.append(s)

    while stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1
    
print("Sad" if stack else "Nice")

        


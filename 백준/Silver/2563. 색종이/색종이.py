n = int(input())
paper = []
x_size = 0
y_size = 0
coord = [[0 for _ in range(100)] for _ in range(100)]


for _ in range(n):
    x, y = map(int, input().split())
    x_size = max(x_size, x)
    y_size = max(y_size, y)

    paper.append([x, y])


for x, y in paper:
    for x_ in range(x, x+10):
        for y_ in range(y, y+10):
            coord[x_][y_] = 1


answer = 0
for row in coord:
    answer += row.count(1)

print(answer)
n, m = map(int, input().split())


answer = []

board = [input() for _ in range(n)]


for i in range(n-7):
    for j in range(m-7):
        s_b = 0
        s_w = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y)%2 ==0:
                    if board[x][y] != "B":
                        s_b += 1
                    if board[x][y] != "W":
                        s_w += 1
                else:
                    if board[x][y] != "W":
                        s_b += 1
                    if board[x][y] != "B":
                        s_w += 1

        answer.append(s_b)
        answer.append(s_w)

print(min(answer))

n, m = map(int, input().split())
square = [list(input()) for _ in range(n)]
mn = min(n, m)
answer = []
while mn != 1:
    s = mn - 1
    for r in range(n - s):
        for c in range(m - s):
            if square[r][c] == square[r + s][c + s] == \
                square[r + s][c] == square[r][c + s]:
                answer.append(mn)
    
    mn -= 1

print(max(answer)**2 if answer else 1)
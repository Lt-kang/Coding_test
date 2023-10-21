l = [input() for _ in range(5)]
answer = ""

for i in range(15):
    for j in range(5):
        try:
            answer += l[j][i]
        except:
            continue


print(answer)




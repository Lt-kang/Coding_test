import sys
input = sys.stdin.readline



l = []
for _ in range(8):
    l.append(int(input()))

temp = l[:]
temp.sort(reverse=True, key=lambda x: (x, x!=0))

print(sum(temp[:5]))
answer = []
for i in range(5):
    answer.append(str(1+l.index(temp[i])))

answer.sort()
print(' '.join(answer))

        
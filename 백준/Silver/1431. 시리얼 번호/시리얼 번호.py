import sys
input = sys.stdin.readline


def sorting(word):
    answer = 0
    for w in word:
        try:
            answer += int(w)
        except:
            continue
    return answer


l = []
for _ in range(int(input())):
    l.append(input())

l.sort(key=lambda x: (len(x), sorting(x), x))

for w in l:
    print(w,end='')
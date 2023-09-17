import sys
input = sys.stdin.readline


word = input()

answer = []

for i in range(len(word)-1):
    answer.append(word[i:-1])

answer.sort()

for w in answer:
    print(w)


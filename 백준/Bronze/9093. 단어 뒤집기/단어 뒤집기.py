import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    sentence = input().split()
    sentence = [word[::-1] for word in sentence]
    print(' '.join(sentence))

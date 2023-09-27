from collections import Counter
import sys; input = sys.stdin.readline


n = int(input())
student = list(input().split())

vote = ""

for _ in range(n):
    vote += input()
    vote += " "

vote = list(vote.split())
vote_counter = Counter(vote)

student.sort(reverse=True, key=lambda x:vote_counter[x])

for i in range(n):
    print(f"{student[i]} {vote_counter[student[i]]}")
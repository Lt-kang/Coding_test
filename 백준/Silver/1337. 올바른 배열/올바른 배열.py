import sys
input = sys.stdin.readline


def right_arr(num, l):
    answer = list(range(num, num+5))
    l_set = set(l)
    answer_set = set(l+answer)
    return abs(len(l_set)-len(answer_set))


n = int(input())
l = [int(input()) for _ in range(n)]

answer = []
for i in l:
    answer.append(right_arr(i, l))

print(min(answer))

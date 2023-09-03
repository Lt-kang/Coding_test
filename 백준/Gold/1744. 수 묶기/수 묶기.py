import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
#l.sort(reverse=True)

pos_l = [i for i in l if i>1]
pos_l.sort(reverse=True)
neg_l = [i for i in l if i<=0]
neg_l.sort()


answer = l.count(1) if 1 in l else 0


for i in range(0,len(pos_l),2):
    if i+1 >= len(pos_l):
        answer += pos_l[i]
    else:
        answer += pos_l[i]*pos_l[i+1]


for j in range(0,len(neg_l),2):
    if j+1 >= len(neg_l):
        answer += neg_l[j]
    else:
        answer += neg_l[j]*neg_l[j+1]


print(answer)
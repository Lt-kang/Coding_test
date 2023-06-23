import sys; input = sys.stdin.readline 

n = int(input())

n_list = [list(map(int,input().split())) for _ in range(n)]
n_list.sort()


time = sum(n_list[0])

for i in range(1,n):
    if time >= n_list[i][0]: time += n_list[i][1]
    else:
        time = sum(n_list[i])

print(time)
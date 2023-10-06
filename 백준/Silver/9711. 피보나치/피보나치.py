import sys; input = sys.stdin.readline

T = int(input())
l = [list(map(int, input().split())) for _ in range(T)]

pibo_index = max(l)[0]+1
pibo = [1]*pibo_index
for i in range(2,pibo_index):
    pibo[i] = pibo[i-1] + pibo[i-2]

for i in range(T):
    print(f"Case #{i+1}: {pibo[l[i][0]-1]%l[i][1]}")
 

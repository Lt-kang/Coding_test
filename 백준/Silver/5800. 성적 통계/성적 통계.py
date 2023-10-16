def neighbor_score(l):
    score = 0
    l.sort()
    for i in range(1, len(l)):
        score = max(l[i]-l[i-1], score)

    return score
        

x = int(input())
l = [list(map(int, input().split())) for _ in range(x)]

for i in range(x):
    temp = l[i][1:]
    print(f"Class {i+1}")
    print(f"Max {max(temp)}, Min {min(temp)}, Largest gap {neighbor_score(temp)}")
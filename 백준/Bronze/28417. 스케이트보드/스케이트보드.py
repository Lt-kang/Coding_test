max_score = 0
for _ in range(int(input())):
    scores = list(map(int, input().split()))

    _run = sorted(scores[:2], reverse=True)
    _trick = sorted(scores[2:], reverse=True)

    max_score = max(max_score, _run[0] + _trick[0] + _trick[1])

print(max_score)


    
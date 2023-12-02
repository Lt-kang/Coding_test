n, score, p = map(int, input().split())


if n == 0:
    answer = 1

else:
    score_ = list(map(int, input().split()))
    score_.append(score)
    score_.sort(reverse=True)

    lenth = len(score_)
    answer = -1

    if p >= lenth:
        for i in range(len(score_)):
            if score == score_[i]:
                answer = i + 1
                break
    elif p < lenth:
        for i in range(p):
            if score == score_[i]:
                if i + score_.count(score_[i]) <= p:
                    answer = i + 1
                    break


print(answer)

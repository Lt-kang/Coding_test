def solution(n, words):
    answer = []
    check_box = []

    for idx, w in enumerate(words):
        if not check_box:
            check_box.append(w)
        elif w in check_box or w[0] != check_box[-1][-1]:
            number = n if (idx+1)%n == 0 else (idx+1)%n
            time = (idx+1)//n if (idx+1)%n == 0 else 1 + (idx+1)//n
            return [number, time]
        elif w not in check_box:
            check_box.append(w)

    return [0, 0]
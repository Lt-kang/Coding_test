def solution(name, yearning, photo):
    memory = {}
    for key, value in zip(name, yearning):
        memory[key] = value

    answer = []
    for p in photo:
        temp = 0
        for i in p:
            try:
                temp += memory[i]
            except:
                continue
        answer.append(temp)
    return answer
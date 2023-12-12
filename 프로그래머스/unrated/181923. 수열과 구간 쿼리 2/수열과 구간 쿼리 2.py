def solution(arr, queries):
    answer = []
    for q in queries:
        mn = 1000000
        temp = 1000000
        for i in range(q[0], q[1] + 1):
            if arr[i] > q[2]:
                temp = min(temp, arr[i])

        if temp != 1000000:
            answer.append(temp)
        elif temp == 1000000:
            answer.append(-1)
            
    return answer
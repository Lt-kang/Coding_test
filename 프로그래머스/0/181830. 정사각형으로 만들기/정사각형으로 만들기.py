def solution(arr):
    r_size, c_size = len(arr), len(arr[0])
    max_size = max(r_size, c_size)

    answer = [[0 for _ in range(max_size)] for _ in range(max_size)]

    for i in range(r_size):
        for j in range(c_size):
            answer[i][j] = arr[i][j]

    return answer
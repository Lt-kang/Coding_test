def solution(arr, queries):
    for i in range(len(queries)):
        for j in range(len(arr)):
            if queries[i][1] >= j >=queries[i][0]: arr[j] += 1
    return arr
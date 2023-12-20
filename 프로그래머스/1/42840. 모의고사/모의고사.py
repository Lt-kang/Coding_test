def solution(answers):
    stu = {'1': 0,
       '2': 0,
       '3': 0}

    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]

    
    for idx, i in enumerate(answers):
        if i == s1[idx % len(s1)]:
            stu['1'] += 1
        if i == s2[idx % len(s2)]:
            stu['2'] += 1
        if i == s3[idx % len(s3)]:
            stu['3'] += 1

    result = []
    mx = max(stu.values())
    for key, value in stu.items():
        if mx == value:
            result.append(int(key))
    
    return result
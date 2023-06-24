def solution(my_strings, parts):
    return ''.join([i[parts[idx][0]:1+parts[idx][1]] for idx, i in enumerate(my_strings)])
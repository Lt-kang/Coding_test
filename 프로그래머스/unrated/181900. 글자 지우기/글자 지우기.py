def solution(my_string, indices):
    return ''.join([w for idx, w in enumerate(my_string) if idx not in indices])
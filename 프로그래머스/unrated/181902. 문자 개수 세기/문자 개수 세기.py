def solution(my_string):
    temp = list(range(ord("A"),ord("Z")+1))+list(range(ord("a"),ord("z")+1))
    return [my_string.count(chr(i)) for i in temp]
def solution(n):
    check_one = bin(n)[2:].count("1")
    while True:
        n += 1
        check = bin(n)[2:].count("1")
        if check == check_one: return n
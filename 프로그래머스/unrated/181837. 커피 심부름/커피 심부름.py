def solution(order):
    return sum([5000 if "latte" in w else 4500 for w in order])
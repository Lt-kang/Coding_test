def solution(dots):
    dots_x = [dots[i][0] for i in range(4)]
    dots_y = [dots[i][1] for i in range(4)]

    return (max(dots_x) - min(dots_x)) * (max(dots_y) - min(dots_y))


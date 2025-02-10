def solution(cards1, cards2, goal):
    sw = True
    for goal_c in goal:
        if cards1 and cards1[0] == goal_c:
            cards1.remove(cards1[0])
        elif cards2 and cards2[0] == goal_c:
            cards2.remove(cards2[0])
        else:
            sw = False

    return "Yes" if sw else "No"
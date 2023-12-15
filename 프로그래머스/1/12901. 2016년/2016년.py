def solution(a, b):
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]   
    return days[((b - 1) + sum(months[:a-1]))%7]
import sys
input = sys.stdin.readline


def calculate_line(a, b):
    return (abs(b[0]-a[0])**2 + abs(b[1]-a[1])**2)


n = int(input())

for _ in range(n):
    l = [list(map(int, input().split())) for _ in range(4)]
    l.sort(key=lambda x: (x[0], x[1]))

    # 대각선의 정의
    # 1. 모든 변의 길이가 같다
    # 2. 모든 대각선의 길이가 같다.

    answer = [calculate_line(l[0], l[1]),
              calculate_line(l[0], l[2]),
              calculate_line(l[0], l[3]),
              calculate_line(l[1], l[2]),
              calculate_line(l[1], l[3]),
              calculate_line(l[2], l[3]),]
    
    answer.sort()
    
    # len(set(answer))==2 => answer의 고유원소는 2개 (변의 길이, 대각선의 길이)
    # answer.count(max(answer))==2 => 대각선의 길이가 제일 길며 그 갯수는 2개
    # answer.count(min(answer))==4 => 변의 길이는 제일 작으며 그 갯수는 4개
    if len(set(answer))==2 and \
        answer.count(max(answer))==2 and \
            answer.count(min(answer))==4: print(1)
    else:
        print(0)




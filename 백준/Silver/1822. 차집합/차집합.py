import sys
input = sys.stdin.readline



n, k = map(int, input().strip().split())

a = set(list(map(int, input().strip().split())))
b = set(list(map(int, input().strip().split())))

print(len(a - b))
print(*sorted(list(a - b)))  # 차집합의 원소를 출력
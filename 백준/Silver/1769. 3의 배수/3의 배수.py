import sys
# input = sys.stdin.readline


n = input()
cnt = 0
while True:
    if len(str(n))==1:
        print(cnt)
        print("YES" if int(n)%3==0 else "NO")
        break
    else:
        n = sum([int(i) for i in str(n)])
        cnt += 1

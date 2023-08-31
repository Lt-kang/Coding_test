def your_result(n, arr):
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp), dp



n=int(input())
arr=list(map(int, input().split()))
cnt, dp = your_result(n, arr)

print(cnt)
answer = []
for i in list(reversed(range(n))):
    if dp[i]==cnt:
        answer.append(arr[i])
        cnt -= 1
answer.reverse()
for w in answer:
    print(w, end=' ')

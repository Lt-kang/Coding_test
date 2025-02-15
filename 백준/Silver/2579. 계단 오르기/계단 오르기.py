

n = int(input())
_list = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(_list[-1])

else:
    dp = [0] * (n + 1)
    dp[1] = _list[1]
    dp[2] = _list[1] + _list[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3] + _list[i-1]) + _list[i]
        '''
        dp[i] = dp[i-2] + _list[i] # -2번째 -> i번째
        dp[i] = dp[i-3] + _list[i-1] + _list[i] # -3번째 -> -1번째 -> i번째
        '''

    print(dp[n])
    
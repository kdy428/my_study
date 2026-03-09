N = int(input())
num = 9901
dp = [0] * (N+1)
if N == 1:
    print(3)
else:
    dp[1] = 3
    tmp = 2
    for i in range(2, N+1):
        dp[i] = (dp[i-1] + 2 * tmp) % num
        tmp += dp[i-1] 

    print(dp[N])

n = int(input())

dp = [-1] * (n+1)
dp[n] = 0
for i in range(n-1, 0, -1):
    if 3 * i <= n:
        dp[i] = min(dp[i+1], dp[2*i], dp[3*i]) + 1

    elif 2 * i <= n:    
        dp[i] = min(dp[i+1], dp[2*i]) +1

    elif i+1 <= n:
        dp[i] = dp[i+1] + 1

print(dp[1])
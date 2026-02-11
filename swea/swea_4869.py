t = int(input())
for tc in range(t):
    n = int(input())
    dp = [0] * 31
    dp[1] = 1
    dp[2] = 3
    nn = n//10
    for i in range(3, nn+1):
        dp[i] = dp[i-1] + 2 * dp[i-2]

    print(f'#{tc+1} {dp[nn]}')
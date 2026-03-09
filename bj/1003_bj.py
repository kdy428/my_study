import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [(0, 0)] * max(2, n+1)
    dp[0] = (1,0)
    dp[1] = (0,1)

    for i in range(2, n+1):
        z1, o1 = dp[i-1]
        z2, o2 = dp[i-2]
        dp[i] = (z1+z2, o1+o2)
    
    print(dp[n][0], dp[n][1])
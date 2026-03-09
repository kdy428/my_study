import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*2 for _ in range(N)]
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[1][0]

    if N >= 2:
        dp[1][0] = dp[0][1] + arr[0][1] 
        dp[1][1] = dp[0][0] + arr[1][1]
    
    for i in range(2,N):
        dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + arr[0][i]
        dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + arr[1][i]

    print(max(dp[N-1]))
T = int(input())
for tc in range(T):
    N = int(input())
    # 0,0부터 n-1,n-1까지 이동하는 최소 합
    # 아래나 위로만 이동 가능
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = arr[0][0]
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j ==0:
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1] + arr[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]

    print(f'#{tc+1} {dp[N-1][N-1]}')
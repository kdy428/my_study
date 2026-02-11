def dfs(i,j,n,arr):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    while True:
        if visited[i][j] == 0:
            visited[i][j] = 1
            cnt += 1
        
        max_d = 0
        for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<n and 0<=nj<n:
                if visited[ni][nj] == 0:
                    if  max_d < arr[i][j] - arr[ni][nj]:
                        max_d = arr[i][j] - arr[ni][nj]
                        next_i = ni
                        next_j = nj
                        
        if max_d != 0:
            i = next_i
            j = next_j
            continue
        else:
            break

    return cnt


t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            val = dfs(i,j,n,arr)
            if ans < val:
                ans = val
    print(f'#{tc+1} {ans}')
def dfs(si,sj,gi,gj,arr):
    visited = [[0]*n for _ in range(n)]
    stack = []
    while True:
        if visited[si][sj] == 0:
            visited[si][sj] = 1
        
        for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
            ni = si + di
            nj = sj + dj
            if 0<=ni<n and 0<=nj<n and visited[ni][nj]==0 and arr[ni][nj] != 1:
                stack.append((si,sj))
                si, sj = ni, nj
                break

        else:
            if stack:
                si, sj = stack.pop()
            else:
                break
            
    if visited[gi][gj] == 1:
        return 1
    else:
        return 0
 
t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 3: # 목표지점
                gi, gj = i, j
            
            if arr[i][j] == 2: # 출발지점
                si, sj = i, j
    
    ans = dfs(si,sj,gi,gj,arr)
    print(f'#{tc+1} {ans}')
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(y, x):
    graph[y][x] = 0
    stack = [(y,x)]
    area = 1
    while stack:
        sy, sx = stack.pop()
        for k in range(4): #방향 4개
            ny, nx = sy+dy[k], sx+dx[k]
            if 0<=ny<n and 0<=nx<m and graph[ny][nx] == 1:
                stack.append((ny,nx))
                graph[ny][nx] = 0
                area += 1
    return area


n, m = map(int, input().split())
#n*m 행렬
graph = [list(map(int, input().split())) for _ in range(n)]

max_area = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            area = dfs(i,j)

            if max_area < area :
                max_area = area

print(cnt)
print(max_area)
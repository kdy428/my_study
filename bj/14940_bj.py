from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# n*m 행렬, 목표지점 2까지의 거리를 표시 bfs 누적합?
si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            si, sj = i, j
            break

def bfs(si, sj, n, m):
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    q.append([si, sj])
    visited[si][sj] = 0
    while q:
        ni, nj = q.popleft()
        for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            wi, wj = ni+di, nj+dj
            if 0<=wi<n and 0<=wj<m:
                if visited[wi][wj] == -1:
                    if arr[wi][wj] == 1:
                        visited[wi][wj] = visited[ni][nj] + 1
                        q.append([wi,wj])
                    elif arr[wi][wj] == 0:
                        visited[wi][wj] = 0
                        q.append([wi,wj])
                if arr[wi][wj] == 0:
                    visited[wi][wj] = 0
                    q.append([wi,wj])
    return visited

visit = bfs(si, sj, n, m)
for i in range(n):
    print(*visit[i])
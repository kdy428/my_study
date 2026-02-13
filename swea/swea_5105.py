from collections import deque

def bfs(si, sj, n):
    visited = [[0] *n for _ in range(n+1)]
    q = deque((si,sj))
    visited[si][sj] = 1
    while True:
        ni, nj = q.leftpop()




t=int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    #스타트지점 2, 도착지점 3
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si, sj = i, j
                break
    bfs(si, sj, n)
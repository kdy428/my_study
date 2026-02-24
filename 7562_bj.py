import sys
from collections import deque
input = sys.stdin.readline

def bfs(si, sj, gi, gj, n):
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    q.append([si,sj])
    visited[si][sj] = 0

    while q:
        si, sj = q.popleft()

        if si == gi and sj == gj:
            return visited[gi][gj]

        for di, dj in [[2,1],[1,2],[-2,1],[1,-2],[2,-1],[-1,2],[-2,-1],[-1,-2]]:
            ni = si + di
            nj = sj + dj
            if 0<=ni<n and 0<=nj<n and visited[ni][nj] == -1:
                visited[ni][nj] = visited[si][sj] + 1
                q.append((ni, nj))
        
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    si, sj = map(int, input().split())
    gi, gj = map(int, input().split())

    print(bfs(si, sj, gi, gj, n))
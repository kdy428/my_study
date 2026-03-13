from collections import deque

t = int(input())
for tc in range(t):
    # 세로 n, 가로 m, 맨홀위치 (r,c), 소요시간 l
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    def f(si, sj, n, m):
        visited = [[-1]*m for _ in range(n)]
        q = deque()
        q.append((si, sj))
        visited[si][sj] = 0
        cnt = 0

        while q:
            ni, nj = q.popleft()
            if 0 <= visited[ni][nj] < l:
                cnt += 1
            if visited[ni][nj] >= l:
                break

            if arr[ni][nj] == 1:
                for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                    wi, wj = ni+di, nj+dj
                    if 0<=wi<n and 0<=wj<m and visited[wi][wj] == -1 and arr[wi][wj] != 0:
                        visited[wi][wj] = visited[ni][nj] + 1
                        q.append((wi, wj))
            elif arr[ni][nj] == 2:
                for di, dj in [[1,0],[-1,0]]:
                    wi, wj = ni+di, nj+dj
                    if 0<=wi<n and 0<=wj<m and visited[wi][wj] == -1 and arr[wi][wj] != 0:
                        visited[wi][wj] = visited[ni][nj] + 1
                        q.append((wi, wj))
            elif arr[ni][nj] == 3:
                for di, dj in [[0,1],[0,-1]]:
                    wi, wj = ni+di, nj+dj
                    if 0<=wi<n and 0<=wj<m and visited[wi][wj] == -1 and arr[wi][wj] != 0:
                        visited[wi][wj] = visited[ni][nj] + 1
                        q.append((wi, wj))
            elif arr[ni][nj] == 4:
                for di, dj in [[1,0],[0,1]]:
                    wi, wj = ni+di, nj+dj
                    if 0<=wi<n and 0<=wj<m and visited[wi][wj] == -1 and arr[wi][wj] != 0:
                        visited[wi][wj] = visited[ni][nj] + 1
                        q.append((wi, wj))
            elif arr[ni][nj] == 5:
                for di, dj in [[-1,0],[0,1]]:
                    wi, wj = ni+di, nj+dj
                    if 0<=wi<n and 0<=wj<m and visited[wi][wj] == -1 and arr[wi][wj] != 0:
                        visited[wi][wj] = visited[ni][nj] + 1
                        q.append((wi, wj))
            elif arr[ni][nj] == 6:
                for di, dj in [[-1,0],[0,-1]]:
                    wi, wj = ni+di, nj+dj
                    if 0<=wi<n and 0<=wj<m and visited[wi][wj] == -1 and arr[wi][wj] != 0:
                        visited[wi][wj] = visited[ni][nj] + 1
                        q.append((wi, wj))
            elif arr[ni][nj] == 7:
                for di, dj in [[1,0],[0,-1]]:
                    wi, wj = ni+di, nj+dj
                    if 0<=wi<n and 0<=wj<m and visited[wi][wj] == -1 and arr[wi][wj] != 0:
                        visited[wi][wj] = visited[ni][nj] + 1
                        q.append((wi, wj))
        return cnt
    print(f'#{tc+1} {f(r,c,n,m)}')
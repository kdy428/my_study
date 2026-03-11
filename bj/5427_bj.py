from collections import deque

t = int(input())
for tc in range(t):
    w, h = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    fire = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                si, sj = i, j
            if arr[i][j] == '*':
                fire.append((i,j))

    def bfs(si, sj, fire, w, h):
        visited = [[[-1]*2 for _ in range(w)] for _ in range(h)]
        q = deque()
        q.append((si,sj))
        visited[si][sj] = [0, 1]
        for i, j in fire:
            q.append((i,j))
            visited[i][j] = [0, 2]
        
        while q:
            # print(visited)
            ni,nj = q.popleft()
            if ni == 0 or ni == h-1 or nj == 0 or nj == w-1:
                if visited[ni][nj][1] == 1:
                    return visited[ni][nj][0]

            for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                wi, wj = ni+di, nj+dj
                if 0<=wi<h and 0<=wj<w and arr[wi][wj] != '#':
                    # 현재 위치가 상근이 일때는 빈곳일때만 이동
                    if visited[ni][nj][1] == 1 and arr[wi][wj] == '.' and  visited[wi][wj][0] == -1:
                        visited[wi][wj] = [visited[ni][nj][0] + 1, 1]
                        q.append((wi,wj))
                    # 현재 위치가 불일때
                    elif visited[ni][nj][1] == 2 and visited[wi][wj][1] != 2:
                        visited[wi][wj] = [visited[ni][nj][0] + 1, 2]
                        q.append((wi,wj))

        return -1
    ans = bfs(si,sj,fire,w,h)
    
    if ans == -1:
        print('IMPOSSIBLE')
        # print('# IMPSSIBLE')
    else:
        print(ans + 1)
        # print('#', ans + 1)
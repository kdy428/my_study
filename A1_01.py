t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    core = []

    # 가장자리 제외한 코어만 저장
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j] == 1:
                core.append((i, j))

    max_core = 0
    min_dist = 1e9

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def can_connect(x, y, dx, dy):
        path = []
        nx, ny = x+dx, y+dy

        while 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] != 0:
                return None
            path.append((nx, ny))
            nx += dx
            ny += dy
        return path

    def set_wire(path, val):
        for x, y in path:
            arr[x][y] = val

    def dfs(idx, core_cnt, dist):
        global max_core, min_dist
        
        if core_cnt + (len(core) - idx) < max_core:
            return
        
        # 모든 코어 확인
        if idx == len(core):
            if core_cnt > max_core:
                max_core = core_cnt
                min_dist = dist
            elif core_cnt == max_core:
                min_dist = min(min_dist, dist)
            return

        x, y = core[idx]

        # 4방향 탐색
        for dx, dy in directions:
            path = can_connect(x, y, dx, dy)

            if path is not None:
                set_wire(path, 2)
                dfs(idx+1, core_cnt+1, dist+len(path))
                set_wire(path, 0)
        # 연결 안 하는 경우
        dfs(idx+1, core_cnt, dist)

    dfs(0, 0, 0)

    print(f"#{tc} {min_dist}")
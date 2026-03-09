def calcu(si, sj, N):
    min_v = 10000
    path = []

    for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
        distan = 0
        tmp = []
        for k in range(1, N):
            wi, wj = si + di*k, sj + dj*k
            if 0<= wi < N and 0<= wj < N:
                if arr[wi][wj] == 0:
                    distan += 1
                    tmp.append((wi, wj))
                else:
                    break
            else:
                if min_v > distan:
                    min_v = distan
                    path = tmp[:]
                break

    if min_v == 10000:
        return -1, []
    
    for wi, wj in path:
        arr[wi][wj] = 2
        
    return min_v, path

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    core = []
    core_cnt = 0
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr[i][j] == 1:
                core.append([i, j])
                core_cnt += 1

    visited = [False] * core_cnt
    min_d = 100000
    max_c = 0
    def func(dist, cnt_core, cnt):
        global min_d, max_c
        
        # 현재값+남은값이 max_c보다 작은경우 가지치기
        if cnt_core + (core_cnt - cnt) < max_c:
            return

        if cnt == core_cnt:
            if max_c < cnt_core:
                max_c = cnt_core
                min_d = dist
            elif max_c == cnt_core and dist < min_d:
                min_d = dist
            return

        for i in range(core_cnt):
            if not visited[i]:
                visited[i] = True
                ni, nj = core[i]
                next_dist, path = calcu(ni, nj, n)

                if next_dist == -1:
                    func(dist, cnt_core, cnt+1)

                else:
                    func(dist+next_dist, cnt_core+1, cnt+1)
                    for wi, wj in path:
                        arr[wi][wj] = 0
                visited[i] = False

    func(0, 0, 0)
    print(f'#{tc+1} {min_d}')
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    visited = [False]*N

    def f(val, cnt):
        global max_v

        if cnt == N:
            if max_v < val:
                max_v = val
            return
        elif val <= max_v:
            return
        else:
            for i in range(N):
                if not visited[i]:
                    visited[i] = True
                    f(val * arr[cnt][i]/100, cnt+1)
                    visited[i] = False

    f(1,0)
    print(f'#{tc+1} {max_v*100:.6f}')
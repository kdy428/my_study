T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [False]* N
    min_d = 10000000

    def f(k, total, cnt):
        global min_d
        if total > min_d:
            return

        if cnt == N-1:
            real_total = total + arr[k][0]
            if min_d > real_total:
                min_d = real_total
            return

        for j in range(1, N):
            if not visited[j]:
                visited[j] = True
                f(j, total + arr[k][j], cnt+1)
                visited[j] = False

    f(0, 0, 0)
    print(f'#{tc+1} {min_d}')
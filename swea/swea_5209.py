for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 1000000
    visited = [False]*N
    def f(sum_v, cnt):
        global min_v
        if cnt == N:
            if min_v > sum_v:
                min_v = sum_v
            return
        elif sum_v > min_v:
            return
        else:
            for i in range(N):
                if not visited[i]:
                    visited[i] =True
                    f(sum_v + arr[cnt][i], cnt+1)
                    visited[i] = False
    f(0,0)
    print(f'#{tc} {min_v}')
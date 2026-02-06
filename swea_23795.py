t = int(input())
for tc in range(t):
    n = int(input())
    ls = [list(map(int, input().split())) for _ in range(n)]

    #i,j가 괴물이면 상하좌우를 벽을 만나기 전까지 3으로 바꿈(볼수있는부분)
    for i in range(n):
        for j in range(n):
            if ls[i][j] == 2:
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    for k in range(1, n):
                        ni = i + di*k
                        nj = j + dj*k
                        if 0<=ni<n and 0<=nj<n:
                            if ls[ni][nj]:
                                break
                            ls[ni][nj] = 3


    # print(ls)
    cnt = 0
    for i in range(n):
        cnt += ls[i].count(0)
    print(f'#{tc+1} {cnt}')
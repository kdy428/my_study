t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    for i in range(n):
        for j in range(n):
            sum_v = arr[i][j]
            for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                for c in range(1, n):
                    ni = i + di * c
                    nj = j + dj * c
                    if 0<=ni<n and 0<=nj<n:
                        sum_v += arr[ni][nj]
                    else:
                        break
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc+1} {max_v}')
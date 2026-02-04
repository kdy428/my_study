t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    for i in range(n):
        for j in range(n):
            # +형태 합 / 조건문으로 인덱스 범위 체크
            s_plus = lst[i][j]
            for k in range(1,m):
                if 0 <= i+k < n:
                    s_plus += lst[i+k][j]
                if 0 <= i-k < n:


                    
                    s_plus += lst[i-k][j]
                if 0 <= j+k < n:
                    s_plus += lst[i][j+k]
                if 0 <= j-k < n:
                    s_plus += lst[i][j-k]
            if max_v < s_plus:
                max_v = s_plus

            # x형태 합 / 조건문으로 인덱스 범위 체크
            sx = lst[i][j]
            for k in range(1,m):
                if 0 <= i+k < n and 0 <= j+k < n:
                    sx += lst[i+k][j+k]
                if 0 <= i-k < n and 0 <= j-k < n:
                    sx += lst[i-k][j-k]
                if 0 <= i+k < n and 0 <= j-k < n:
                    sx += lst[i+k][j-k]
                if 0 <= i-k < n and 0 <= j+k < n:
                    sx += lst[i-k][j+k]
            
            if max_v < sx:
                max_v = sx
    
    print(f'#{tc+1} {max_v}')
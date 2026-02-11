for _ in range(10):
    tc = int(input())

    lst = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    #행 확인
    for i in range(100):
        s = 0
        for j in range(100):
            s += lst[i][j]
        if max_sum < s:
            max_sum = s

    #열 확인
    for i in range(100):
        s = 0
        for j in range(100):
            s += lst[j][i]
        if max_sum < s:
            max_sum = s
    
    #오른쪽 아래 대각선 확인
    s = 0
    for i in range(100):
        s += lst[i][i]
    if max_sum < s:
        max_sum = s

    #왼쪽 아래 대각선 확인
    s = 0
    for i in range(100):
        s += lst[i][99-i]
    if max_sum < s:
        max_sum = s

    print(f'#{tc} {max_sum}')
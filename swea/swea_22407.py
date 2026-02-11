t = int(input())
for tc in range(t):
    num_lst = [[0]*10 for _ in range(10)]
    for color in range(1,3): #첫번째반복 빨강 1, 두번째반복 파랑 2
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                num_lst[i][j] += color

    # w는 가로 길이(j), h는 세로 길이(i)
    lst_i = []
    lst_j = []
    for i in range(10):
        for j in range(10):
            if num_lst[i][j] == 3:
                lst_i.append(i)
                lst_j.append(j)

    if not lst_i:
        print(f'#{tc + 1} 0 0')

    else:
        w = max(lst_j)-min(lst_j) +1
        h = max(lst_i)-min(lst_i) +1
        print(f'#{tc + 1} {w} {h}')


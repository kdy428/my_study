t = int(input())

for tc in range(t):
    n = int(input())
    zero_lst = [[0]*10 for _ in range(10)]

    for k in range(n):
        x1, y1, x2, y2, num = map(int, input().split())

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if zero_lst[i][j] == 0:
                    zero_lst[i][j] = num
                elif zero_lst[i][j] == 1:
                    if num == 2:
                        zero_lst[i][j] += num
                else:
                    if num == 1:
                        zero_lst[i][j] += num

    cnt = 0
    for i in range(10):
        for j in range(10):
            if zero_lst[i][j] == 3:
                cnt += 1

    print(f'#{tc+1} {cnt}') 
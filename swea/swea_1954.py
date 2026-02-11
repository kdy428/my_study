t = int(input())

for tc in range(t):
    n = int(input())

    output_lst = [[0]*n for _ in range(n)]
    output_lst[0][0] = 1

    my_pos = [0, 0]
    my_dir = [0, 1]

    #동남서북
    dir_x = [0, 1 , 0, -1]
    dir_y = [1, 0, -1, 0]

    cnt = 1
    i = 0
    while cnt < (n*n):
        # 인덱스 범위를 벗어나거나, 앞에 있는 칸의 값이 0이 아닌 경우
        # x,y 인덱스를 하나씩 밀어서 my_dir을 수정
        if my_pos[0] + my_dir[0] >= n or my_pos[1] + my_dir[1] >= n:
            i += 1
            i = i % 4
            my_dir[0] = dir_x[i]
            my_dir[1] = dir_y[i]
        
        elif output_lst[my_pos[0] + my_dir[0]][my_pos[1] + my_dir[1]] != 0 :
            i += 1
            i = i % 4
            my_dir[0] = dir_x[i]
            my_dir[1] = dir_y[i]


        my_pos[0] += my_dir[0]
        my_pos[1] += my_dir[1]
        cnt += 1
        output_lst[my_pos[0]][my_pos[1]] = cnt

    print(f'#{tc+1}')
    for i in range(n):
        print(*output_lst[i])

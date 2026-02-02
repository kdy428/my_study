t = int(input())

for tc in range(t):
    num = int(input())
    num_lst = list(map(int, input().split()))

    max_num = num_lst[0]
    min_num = num_lst[0]

    for i in num_lst:
        if max_num < i:
            max_num = i
        
        if min_num > i :
            min_num = i
    print(f'#{tc+1} {max_num-min_num}')
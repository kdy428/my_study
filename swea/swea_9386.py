t = int(input())

for tc in range(t):
    n = int(input())
    num_lst = list(map(int, input()))
    # print(num_lst)

    max_one = 0
    cnt = 0
    for num in num_lst:
        if num == 1:
            cnt += 1
        
        else:
            if max_one < cnt:
                max_one = cnt
                
            cnt = 0
    
    if max_one < cnt:
        max_one = cnt
    
    print(f'#{tc+1} {max_one}')
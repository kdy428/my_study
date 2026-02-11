t = int(input())

for tc in range(t):
    n = int(input())
    num_lst = list(map(int, input().split()))
    cnt_lst= []

    for i in range(len(num_lst)):
        temp = num_lst[i]
        cnt = 0

        while i < n-1:
            i += 1
            if temp > num_lst[i]:
                cnt += 1
        
        cnt_lst.append(cnt)
    
    print(f'#{tc+1} {max(cnt_lst)}')
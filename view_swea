for tc in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    for i in range(2, n-2):
        new_lst = [lst[i-2], lst[i-1], lst[i+1], lst[i+2]]
        if max(new_lst) < lst[i]:
            cnt += lst[i] - max(new_lst)
    
    print(f'#{tc+1} {cnt}')

for tc in range(10):
    n = int(input())
    num_lst = list(map(int, input().split()))

    for _ in range(n):
        num_lst[num_lst.index(max(num_lst))] -= 1
        num_lst[num_lst.index(min(num_lst))] += 1
    
    print(f'#{tc+1} {max(num_lst)-min(num_lst)}')
t = int(input())

for tc in range(t):
    n = int(input())
    num_lst = list(map(int, input().split()))

    for i in range(n):
        for j in range(n-i-1):
            if num_lst[j] > num_lst[j+1]:
                num_lst[j], num_lst[j+1] = num_lst[j+1], num_lst[j]

    print(f'#{tc+1}', end=' ')
    print(*num_lst)
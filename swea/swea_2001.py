t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_v = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            # new_lst = []
            sum_v = 0

            for k in range(m):
                for l in range(m):
                    # new_lst.append(arr[i+k][j+l])
                    sum_v += arr[i+k][j+l]

            # print(new_lst)
            # sum_v = sum(new_lst)

            if max_v < sum_v:
                max_v = sum_v
    
    print(f'#{tc+1} {max_v}')
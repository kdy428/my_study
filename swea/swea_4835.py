t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    num_lst = list(map(int, input().split()))

    max_sum = 0
    min_sum = sum(num_lst)

    for i in range(n-m+1):
        if max_sum < sum(num_lst[i : i+m]):
            max_sum = sum(num_lst[i : i+m])
        
        if min_sum > sum(num_lst[i : i+m]):
            min_sum = sum(num_lst[i : i+m])
    
    output = max_sum - min_sum
    print(f'#{tc+1} {output}')
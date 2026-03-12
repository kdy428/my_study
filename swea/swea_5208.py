for tc in range(1, int(input())+1):
    arr = list(map(int, input().split())) + [0]
    N = arr.pop(0)
    dp = [-1]*N

    i = N-1
    cnt = 0
    while i != 0:
        j = 0
        while True:
            if j + arr[j] >= i:
                for k in range(j, i):
                    dp[k] = cnt
                break
            j += 1
        i = j
        cnt += 1
        
    print(f'#{tc} {dp[0]}')
t = int(input())
for tc in range(t):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    min_v = 1000000

    def f(cnt, sum_v):
        global min_v
        if cnt == n:
            if sum_v >= b and min_v > sum_v - b:
                min_v = sum_v - b
        else:
            f(cnt + 1, sum_v + arr[cnt])
            f(cnt + 1, sum_v)

    f(0,0)
    print(f'#{tc+1} {min_v}')
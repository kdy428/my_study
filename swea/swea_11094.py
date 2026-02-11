t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    for i in range(n):
        sum_i = 0
        sum_j = 0
        for j in range(n):
            sum_i += arr[i][j]
            sum_j += arr[j][i]
        
        if max_v < sum_i:
            max_v = sum_i
        if max_v < sum_j:
            max_v = sum_j
        
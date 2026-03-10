t = int(input())
for tc in range(t):
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = map(int, input().split())
        lst.append([a, b])
    lst.sort(key=lambda x: x[1])
    tmp = 0
    i = 0
    cnt = 0
    while tmp <= 24 and i < n:
        if lst[i][0] >= tmp:
            tmp = lst[i][1]
            cnt += 1
        i += 1
        
    print(f'#{tc+1} {cnt}')
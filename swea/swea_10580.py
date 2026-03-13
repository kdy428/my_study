t = int(input())
for tc in range(t):
    n = int(input())
    lst = []
    cnt = 0
    for _ in range(n):
        left, right = map(int, input().split())
        for l, r in lst:
            if left < l and right > r:
                cnt += 1
            if left > l and right < r:
                cnt += 1
        lst.append([left, right])

    print(f"#{tc+1} {cnt}")
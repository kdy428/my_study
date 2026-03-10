t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    n_lst = sorted(list(map(int, input().split())))
    m_lst = sorted(list(map(int, input().split())))
    i = n-1
    j = m-1
    total = 0
    while i >= 0 and j >= 0:
        if m_lst[j] >= n_lst[i]:
            total += n_lst[i]
            i -= 1
            j -= 1
        elif m_lst[j] < n_lst[i]:
            i -= 1
    print(f'#{tc+1} {total}')
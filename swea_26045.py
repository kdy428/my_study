t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))

    answer = 'NO'
    i = 0
    j = 0

    while not (i == n or j == m) :
        if m_lst[j] == n_lst[i]:
            i += 1
            j += 1
        else:
            i += 1

    if j == m :
        answer = 'YES'

    print(f'#{tc+1} {answer}')

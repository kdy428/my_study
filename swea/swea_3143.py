t = int(input())
for tc in range(t):
    a, b = map(str, input().split())
    a_lst = list(a)
    b_lst = list(b)

    i = 0
    cnt = 0
    while i < len(a_lst):
        if a_lst[i] == b_lst[0] and i <= (len(a_lst)-len(b_lst)):
            for j in range(1, len(b_lst)):
                if a_lst[i + j] != b_lst[j]:
                    break
            else:
                cnt += 1
                i += len(b_lst)
                continue
        i += 1
        cnt += 1

    print(f'#{tc+1} {cnt}')

# # '-'.join(a.split(b))
# # a를 b를 기준으로 나누고 -로 연결 후 len
# t = int(input())
# for tc in range(1, t+1):
#     a, b = input().split()
#     print(f'#{tc}', len('-'.join(a.split(b))))

# # a.replace(b, '-')
# # a내부의 b를 -로 교체 후 len
# t = int(input())
# for tc in range(1, t+1):
#     a, b = map(str, input().split())
#     n_a = a.replace(b, '-')
#     print(f"#{tc} {len(n_a)}")
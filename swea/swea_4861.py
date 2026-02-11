t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    str_lst = [list(map(str, input())) for _ in range(n)]
    # n*n에서 길이가 m인 회문 찾기

    #가로 검사
    for i in range(n):
        for j in range(n-m+1):
            for k in range(m):
                if str_lst[i][j+k] != str_lst[i][j+m-k-1]:
                    break
            else:
                ans = ''.join(str_lst[i][j:j + m])
                break


    #세로 검사
    for i in range(n):
        for j in range(n-m+1):
            for k in range(m):
                if str_lst[j+k][i] != str_lst[j+m-k-1][i]:
                    break
            else:
                ans = ''.join(str_lst[j+r][i] for r in range(m))
                break

    print(f'#{tc+1} {ans}')

# t = int(input())
# for tc in range(t):
#     n, m = map(int, input().split())
#     str_lst = [list(map(str, input())) for _ in range(n)]
#     # n*n에서 길이가 m인 회문 찾기
#     ans = None
#     find = False
#     #가로 검사
#     for i in range(n):
#         for j in range(n-m+1):
#             for k in range(m):
#                 if str_lst[i][j+k] != str_lst[i][j+m-k-1]:
#                     break
#             else:
#                 ans = ''.join(str_lst[i][j:j + m])
#                 find = True
#                 break
#         if find:
#             break
 
#     #세로 검사
#     if ans is None:
#         find = False
#         for i in range(n):
#             for j in range(n-m+1):
#                 for k in range(m):
#                     if str_lst[j+k][i] != str_lst[j+m-k-1][i]:
#                         break
#                 else:
#                     ans = ''.join(str_lst[j+r][i] for r in range(m))
#                     find = True
#                     break
#             if find:
#                 break
     
#     print(f'#{tc+1} {ans}')
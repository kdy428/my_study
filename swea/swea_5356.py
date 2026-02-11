t = int(input())
for tc in range(t):
    output_lst = [list(map(str, input())) for _ in range(5)]

    length_lst = [len(output_lst[0]), len(output_lst[1]), len(output_lst[2]), len(output_lst[3]), len(output_lst[4])]

    print(f'#{tc+1}', end=' ')
    for i in range(max(length_lst)):
        for j in range(5):
            if i > len(output_lst[j])-1:
                continue
            else:
                print(output_lst[j][i], end='')
    print()


# for tc in range(1, int(input())+1):
#     arr = [input() for _ in range(5)]
#     ans = ''
#     for j in range(15):
#         for i in range(5):
#             if 0 <= j < len(arr[i]):
#                 ans += arr[i][j]
 
#     print(f'#{tc} {ans}')
t=int(input())
for tc in range(t):
    key_lst = list(map(str, input()))
    str_lst = list(map(str, input()))

    find = 0
    for i in range(len(str_lst)-len(key_lst)+1):
        for j in range(len(key_lst)):
            if str_lst[i+j] != key_lst[j]:
                break
        else:
            find = 1
            break
    
    print(f'#{tc+1} {find}')
t = int(input())
for tc in range(t):
    str1 = list(set(map(str, input())))
    str2 = list(map(str, input()))

    num_lst = [0] * len(str1)

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                num_lst[i] += 1

    print(f'#{tc+1} {max(num_lst)}')
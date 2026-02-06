t = int(input())
for tc in range(t):
    lst = list(map(str, input()))
    ans = 1
    for i in range(len(lst)//2):
        if lst[i] != lst[len(lst)-i-1]:
            ans = 0
            break
    print(f'#{tc+1} {ans}')

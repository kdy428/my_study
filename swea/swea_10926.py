def func(lst):
    lst.reverse()
    num = 0
    for i in range(7):
        if lst[i]:
            num += 2**i
    return num

t = int(input())
for tc in range(t):
    arr = list(map(int, input()))
    ans = []
    for i in range(0, len(arr), 7):
        ans.append(func(arr[i:i+7]))
    
    print(f'#{tc+1}', *ans)
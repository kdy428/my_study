def pas(arr, cnt):
    if cnt == 0:
        return []
    new_arr = [1]

    for i in range(len(arr) - 1):
        new_arr.append(arr[i] + arr[i+1])
    new_arr.append(1)
    
    return [arr] + pas(new_arr, cnt - 1)
    
t = int(input())
for tc in range(t):
    n = int(input())
    arr = [1]
    output_lst = pas(arr, n)
    
    print(f'#{tc+1}')
    for i in range(n):
        print(*output_lst[i])
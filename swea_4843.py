t = int(input())
for tc in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n-1):
        for j in range(1, n-i):
            if i % 2 == 0: #짝수 항의 경우
                if lst[i] < lst[i+j]:
                    lst[i], lst[i+j] = lst[i+j], lst[i]
            else: #홀수 항의 경우
                if lst[i] > lst[i+j]:
                    lst[i], lst[i+j] = lst[i+j], lst[i]
    
    print(f'#{tc+1} {" ".join(map(str, lst[:10]))}')
        
    # print(f'#{tc+1}', *lst[:10])
    # print(f'#{tc+1}', end=' ')
    # print(*lst)


# T = int(input())

# def selection_sort(arr, N):
#     for i in range(10):
#         idx = i
#         for j in range(i + 1, N):
#             if i % 2 == 0:
#                 if arr[idx] < arr[j]:
#                     idx = j
#             else:
#                 if arr[idx] > arr[j]:
#                     idx = j
#         arr[i], arr[idx] = arr[idx], arr[i]
#     return arr[:10]


# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     # arr.sort()

#     A = selection_sort(arr, N)

#     print(f'#{tc}', *A)
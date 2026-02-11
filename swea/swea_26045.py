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


# t = int(input())
# for tc in range(t):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     max = 0
#     len = 0
#     result = 'NO'
 
#     for i in range(M): #0번째 뽑아
#         for j in range(max, N):
#             if B[i] == A[j]:
#                 max = j+1
#                 len += 1
#                 break
    
#     if len == M:
#         result = 'YES'
     
#     print(f'#{tc+1} {result}')


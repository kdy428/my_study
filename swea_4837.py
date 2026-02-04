from itertools import combinations

t = int(input())

for tc in range(t):
    n, k = map(int, input().split())

    num_lst = []
    for i in range(1,k+1):
        num_lst.append(i)
    # print(num_lst)
    cnt = 0
    lst = list(combinations(num_lst, n))
    # print(lst)
    
    for num in lst:
        if k == sum(num):
            cnt +=1

    print(f'#{tc+1} {cnt}')

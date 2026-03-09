from itertools import combinations

def f(number_list, cnt):
    global max_v
    cur_str = ''.join(number_list)
    cur_val = int(cur_str)
    
    if (cur_str, cnt) in visited:
            return
    visited.add((cur_str, cnt))

    if cnt == n:
        if cur_val > max_v:
            max_v = cur_val
        return
    
    for i, j in combinations(range(len(lst)), 2):
        number_list[i], number_list[j] = number_list[j], number_list[i]
        f(number_list, cnt+1)
        number_list[i], number_list[j] = number_list[j], number_list[i]

T = int(input())
for tc in range(T):
    data, n = input().split()
    lst = list(data)
    n = int(n)

    max_v = 0
    visited = set()
    f(lst, 0)

    print(f'#{tc+1} {max_v}')
t = int(input())

for tc in range(t):
    n = int(input())
    num_lst = list(map(int, input()))
    counts = [0] * (max(num_lst)+1)

    for i in range(n):
        counts[num_lst[i]] += 1
    
    cnt = 0
    lst = []
    for i in range(len(counts)):
        if max(counts) == counts[i] : # counts의 최대 val를 가지는 인덱스가 2개이상이라면,
            lst.append(i)
            cnt += 1
        

    if cnt >= 2:
        print(f'#{tc+1} {max(lst)} {max(counts)}')
    else :
        print(f'#{tc+1} {counts.index(max(counts))} {max(counts)}')
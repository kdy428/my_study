#i,j로 영역을 나눔
#0~i영역은 소, i~j영역은 중, j~n-1영역은 대
#i는 0~(n-3)까지, j는 (i+1)~(n-2)
t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()

    min_v = 1000
    for i in range(n-2):
        for j in range(i+1, n-1):
            if arr[i] == arr[i+1] or arr[j] == arr[j+1]:
                continue
            s = i + 1
            m = j - i
            l = n - 1 - j

            if min_v > (max(s,m,l) - min(s,m,l)):
                min_v = max(s,m,l) - min(s,m,l)

    if min_v == 1000:
        print(f'#{tc+1} -1')
    else:
        print(f'#{tc+1} {min_v}')
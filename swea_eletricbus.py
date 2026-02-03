t = int(input())

for tc in range(t):
    #k는 한번 충전으로 이동할 수 있는 정류장 수, n은 정류장 수 0~n, m은 충전기 수
    # 최소한의 충전으로 종점에 도착할 수 있는지 출력
    k, n, m = map(int, input().split())
    num_lst = list(map(int, input().split())) #충전기가 설치된 정류장 번호
    
    lst = [0] * n # n개의 배열

    for i in range(len(lst)):
        for num in num_lst:
            if i == num:
                lst[i] = 1
    # 충전기가 있는 위치 1, 없는 위치 0인 리스트 생성

    my_idx = 0
    cnt = 0
    while my_idx+k < n:
        if sum(lst[my_idx+1 : my_idx+k+1]) >= 1:
            cnt += 1 
            for i in range(k, 0, -1):
                if lst[my_idx+i] == 1:
                    my_idx += i
                    break

        else:
            cnt = 0
            break
    
    print(f'#{tc+1} {cnt}')
#IM 모의 1
t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    max_area = 0
    for j in range(n):
        for i in range(n):
            for k in range(1,n):
                for l in range(1,n):
                    # i,j로 부터 k,l 거리를 조사하며 temp과 같은 값을 찾음
                    if 0<=i+l<n and 0<=j+k<n:
                        if arr[i][j] == arr[i+l][j+k]:
                            area = l * k # 증가한 거리를 통해 area 확인
                            if max_area < area: # 기존 max_area보다 큰 경우, 값을 바꾸고 cnt = 1
                                cnt = 1
                                max_area = area
                            elif max_area == area: # 기존과 동일한 경우 cnt += 1
                                cnt += 1
                            # max_area보다 작은 area에 대해서는 pass(무시)
    if cnt != 0:
        print(f'#{tc+1} {cnt}')
    else:
        print(f'#{tc+1} {n*n}')
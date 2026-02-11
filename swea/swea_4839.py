def binary_search(N, goal):
    start = 1
    end = N
    cnt = 0
    while start <= end:
        mid = int((start + end) / 2)
        cnt += 1
        if mid == goal:
            return cnt
        elif mid > goal: #왼쪽구간에 goal가 있는 경우
            end = mid
        else: #오른쪽구간에 goal가 있는 경우
            start = mid
    
t = int(input())
for tc in range(t):
    # 전체 쪽수 1~p, a가 찾을 쪽수, b가 찾을 쪽수
    p, a, b = map(int, input().split())
    
    cnt_a = binary_search(p, a)
    cnt_b = binary_search(p, b)
    # print(cnt_a, cnt_b)
    #빨리 찾으면 승리(cnt값이 작으면 승리)
    if cnt_a < cnt_b:
        print(f'#{tc+1} A')
    elif cnt_a > cnt_b:
        print(f'#{tc+1} B')
    else:
        print(f'#{tc+1} 0')

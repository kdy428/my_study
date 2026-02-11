t = int(input())

for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0 #첫 일꾼의 마지막 영역
    min_v = 1000000 #두 구역 최소 차이
    for i in range(0, n-1): #왼쪽 구역의 경계
        left = sum(arr[:i+1])
        right = sum(arr[i+1:])
        if min_v > abs(left-right):
            min_v = abs(left-right)
            ans = i + 1 #영역은 1번부터 시작
    print(f'#{tc+1} {ans} {min_v}')
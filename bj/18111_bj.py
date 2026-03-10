import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]







T = int(input())
for tc in range(1, T+1):
    N = int(input())        # N x N
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_battery = 10000
    used = [False] * (N+1)

    def f(x, last, s):      # x: 시작, last: 마지막 위치, s: sum
        global min_battery

        # 가지치기
        if s >= min_battery:
            return

        # 모든 구역을 다 돌았다면?
        if x == N:
            # 마지막 구역에서 1번 사무실로 돌아가는 비용 추가
            total = s + arr[last-1][0]
            if min_battery > total:
                min_battery = total
            return

        # 2번부터 N번 구역까지
        for i in range(2, N+1):
            if not used[i]:
                used[i] = True
                # f(다음 단계, 현재 방문한 구역 i, 현재까지 합 + 이동 비용)
                f(x+1, i, s + arr[last-1][i-1])
                used[i] = False


    f(1, 1, 0)

    print(f'#{tc} {min_battery}')
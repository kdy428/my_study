# 금맥을 발견하면 bfs를 활용하여 배열의 값을 더하고 크기는 카운팅
def bfs(si, sj):
    global max_sum, max_size
    q = []
    q.append([si,sj])
    sum_v = arr[si][sj]     # 현재 위치 값을 초기값으로 설정
    size_v = 1              # 사이즈는 현재위치를 포함한 1로 설정
    arr[si][sj] = -1        # arr에 현재 위치 방문 표시

    while q:
        # 큐는 선입선출 구조로 0번 인덱스의 값을 pop 시킴
        ni, nj = q.pop(0)
        for di, dj in [[1, 0], [0, -1], [-1, 0], [0, 1]]:  # 상하좌우 델타행렬
            wi, wj = ni + di, nj + dj
            if 0 <= wi < n and 0 <= wj < n:
                if arr[wi][wj] in [1,2,3]:
                    q.append([wi,wj])
                    sum_v += arr[wi][wj]
                    size_v += 1
                    # 방문한 곳은 -1로 표시
                    arr[wi][wj] = -1
    # while문이 끝나면 max값 비교를 통해 최댓값 갱신
    if max_sum < sum_v:
        max_sum = sum_v
        max_size = size_v
    if max_sum == sum_v:
        max_size = min(max_size, size_v)

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_sum = 0
    max_size = 0

    # 전체 배열을 탐색하며 금맥을 찾으면 bfs함수 실행
    for i in range(n):
        for j in range(n):
            if arr[i][j] in [1,2,3]:
                bfs(i,j)
    print(f'#{tc+1} {max_sum} {max_size}')

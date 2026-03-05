# 술래를 찾고 델타행렬을 활용하여 통로를 1로 채움
def search(si, sj):
    for di, dj in [[1, 0], [0, -1], [-1, 0], [0, 1]]:
        for k in range(1,n):
            ni, nj = si + di * k, sj + dj * k
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
                arr[ni][nj] = 1
            # arr의 값이 통로가 아닌 경우, 해당 방향 break
            else:
                break

t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # arr에서 술래인 위치를 찾고, search 함수를 실행
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                search(i,j)
    # arr을 탐색하며 통로(0)로 남아있는 개수를 카운팅
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                cnt += 1
    print(f'#{tc+1} {cnt}')


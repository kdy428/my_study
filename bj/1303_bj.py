import sys
input = sys.stdin.readline

def bfs(si, sj, st):
    global visited
    stack = []
    stack.append((si, sj))
    cnt = 0

    while stack:
        if arr[si][sj] == st:
            arr[si][sj] = 'C'
            cnt += 1

        for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni = si + di
            nj = sj + dj
            if 0<=ni<m and 0<=nj<n and arr[ni][nj] == st:
                stack.append((si,sj))
                si, sj = ni, nj
                break
        else:
            si, sj = stack.pop()
    
    return cnt**2


# n 가로, m 세로
n, m = map(int,input().split())
# W,B 출력

arr = [list(map(str, input().strip())) for _ in range(m)]

ans_w, ans_b = 0, 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == 'Y':
            continue
        elif arr[i][j] == 'W':
            ans_w += bfs(i, j, 'W')
        elif arr[i][j] == 'B':
            ans_b += bfs(i, j, 'B')

print(ans_w, ans_b)

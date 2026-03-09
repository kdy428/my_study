import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False]*N
min_v = 10000000

def calculate():
    start = 0
    link = 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                start += arr[i][j]
            elif not visited[i] and not visited[j]:
                link += arr[i][j]
    return abs(start - link)


def func(idx, cnt):
    global min_v
    if cnt == N //2 :
        min_v = min(min_v, calculate())
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            func(i+1, cnt+1)
            visited[i] = False

visited[0] = True
func(1, 1)
print(min_v)
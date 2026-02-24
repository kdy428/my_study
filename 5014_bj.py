import sys
from collections import deque
input = sys.stdin.readline

def bfs(start,goal):
    visited = [-1] * (f+1)
    q = deque([start])
    visited[start] = 0
    ans = 0

    while q:
        now = q.popleft()

        if now == goal:
            ans = 1
            break
        
        if now+u <= f:
            if visited[now+u] == -1:
                visited[now+u] = visited[now] + 1
                q.append(now+u)
        if 0 < now-d:        
            if visited[now-d] == -1:
                visited[now-d] = visited[now] + 1
                q.append(now-d)

    if ans:
        return visited[goal]
    else:
        return -1
    
# f 건물 층수, g 스타링크위치 층, s 현재 위치
# 엘베 버튼 위로 u층, 아래로 d층
# g 층에 갈 수 없다면 "use the stairs" 출력
f, s, g, u, d = map(int, input().split())

cnt = bfs(s,g)
if cnt == -1:
    print('use the stairs')
else:
    print(cnt)
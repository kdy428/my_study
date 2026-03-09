import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(s, n):
    visited = [0] * (n+1)
    q = deque([s])
    cnt = 0
    while q:
        n = q.popleft()
        cnt += 1
        visited[n] = cnt
        for w in d[n]:
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)

    return visited[1:]


# 노드 n, 간선 m, 시작 r
n, m, r = map(int, input().split())
d = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

for i in d.keys():
    d[i].sort()

ans = bfs(r, n)
print(*ans, sep='\n')  
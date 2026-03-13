import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
adj_lst = [[] for _ in range(n)]
# 출발 도시, 도착 도시, 버스 비용
# 출발도시, 도착 도시
for i in range(m):
    a, b, c = map(int, input().split())
    adj_lst[a].append((b, c))
# print(adj_lst)
start, end = map(int, input().split())

visited = [False]*(n+1)
min_v = 1000000000
def back(s, cost):
    global min_v
    if min_v < cost:
        return
    
    if s == end:
        if min_v > cost:
            min_v = cost
        return
    
    for w, c in adj_lst[s]:
        if not visited[w]:
            visited[w] = True
            back(w, c)
            visited[w] = False

back(start, 0)

print(min_v)
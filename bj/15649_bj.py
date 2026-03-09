n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
visited = [False]*n
lst = []
def func(cnt):
    if cnt == m:
        print(*lst)
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            lst.append(arr[i])
            func(cnt+1)
            lst.pop()
            visited[i] = False
func(0)
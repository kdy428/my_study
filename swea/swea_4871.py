def dfs(v, s, n):
    visited = [0] * (v+1)
    stack = []

    while True:
        if visited[s] == 0:
            visited[s] = 1

        for w in adj_lst[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w
                break
        
        else:
            if stack:
                s = stack.pop()
            else:
                break

    if visited[n] == 1:
        return 1
    else:
        return 0

t = int(input())
for tc in range(t):
    # V개의 노드를 E개의 연결
    V, E = map(int, input().split())
    
    adj_lst = [[] for _ in range(V+1)]
    for _ in range(E):
        c1, c2 = map(int,input().split())
        adj_lst[c1].append(c2)
        # adj_lst[c2].append(c1)

    S, G = map(int,input().split())

    ans = dfs(V, S, G)
    print(f'#{tc+1} {ans}')
from collections import defaultdict

def dfs(s):
    visited = [0] * 100
    stack = []

    while True:
        if visited[s] == 0:
            visited[s] = 1
        
        for w in d[s]:
            if visited[w] == 0:
                stack.append(s)
                s = w
                break
        
        else:
            if stack:
                s = stack.pop()
            else:
                break

    if visited[99] == 1:
        return 1
    else:
        return 0

# 일방통행, A에서 B까지 가는 길
for _ in range(10):
    #테스트케이스 번호, m개의 연결
    tc, m = map(int, input().split())
    lst = list(map(int, input().split()))

    d=defaultdict(list)
    for i in range(m):
        c1, c2 = lst[2 * i], lst[2 * i + 1]
        d[c1].append(c2)
    
    ans = dfs(0)

    print(f'#{tc} {ans}')

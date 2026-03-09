from collections import deque

def f(s):
    q = deque([s])
    visited = [-1] * (s+1)
    visited[s] = 0
    while q:
        s = q.popleft()

        if s == 1:
            break
        if s % 3 == 0:
            w = s//3
            if visited[w] == -1:
                visited[w] = visited[s] + 1
                q.append(w)
        
        if s % 2 == 0:
            w = s//2
            if visited[w] == -1:
                visited[w] = visited[s] + 1
                q.append(w)
        
        if visited[s-1] == -1:
            visited[s-1] = visited[s] + 1 
            q.append(s-1)

    return visited[1]

n = int(input())

print(f(n))
arr = [i for i in range(1, 7)]

def f(ans, cnt):
    if cnt == 3:
        print(*ans)
        return
    
    for i in arr:
        ans.append(i)
        f(ans, cnt+1)
        ans.pop()
f([], 0)
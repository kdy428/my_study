import sys
input = sys.stdin.readline

# N개의 카드, K개 선택
N = int(input())
K = int(input())
lst = [input().strip() for _ in range(N)]

visit = [False] * N
check_set = set()

def f(ans, cnt):
    if cnt == K:
        check_set.add(ans)
        return
    
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            f(ans+lst[i],cnt+1)
            visit[i] = False
    
f('', 0)
print(len(check_set))
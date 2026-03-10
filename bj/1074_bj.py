import sys
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())

cnt = 0

# 2*2까지 분할하는 함수
def f(si, sj, size):
    global cnt

    if not (si <= r < si + size and sj <= c < sj + size):
        cnt += size * size
        return
    
    if size == 1:
        if si == r and sj == c:
            print(cnt)
            exit() # 정답을 찾으면 즉시 종료
        cnt += 1
        return
    
    mid = size // 2
    f(si, sj, mid)           # 왼쪽 위
    f(si, sj + mid, mid)     # 오른쪽 위
    f(si + mid, sj, mid)     # 왼쪽 아래
    f(si + mid, sj + mid, mid)
    
f(0,0,2**n)
import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
d = defaultdict(int)
# 중복순열
def f(k, ans, cnt):
    if cnt == m:
        if d[*ans] == 0:
            d[*ans] += 1
            print(*ans)
        return
    for i in range(k, n):
        ans.append(arr[i])
        f(i ,ans, cnt+1)
        ans.pop()
f(0, [], 0)
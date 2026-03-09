import sys
input = sys.stdin.readline
    

# n줄, k원
n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

ans = 0
for i in range(n-1, -1, -1):
    ans += k // arr[i]
    k %= arr[i]

print(ans)
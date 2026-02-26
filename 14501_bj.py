n = int(input()) # 남은 퇴사일
lst = []
for i in range(n):
    x, y = map(int, input().split())
    lst.append([x,y])

dp = [0] * (n+1)

for i in range(n):
    nd = lst[i][0]
    nv = lst[i][1]
    dp[i+nd] = max()
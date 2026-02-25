n = int(input())
num = 15746
# 1인 타일은 단일, 0인 타일은 00 묶어서
dp = [0] * (n+1)
dp[1]=1
if n >= 2:
    dp[2]=2
for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2])%num
print(dp[n])
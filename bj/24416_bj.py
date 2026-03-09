n = int(input())

# cnt_dp: dp[3]~dp[n] 계산 횟수
cnt_dp = n - 2

if n == 1 or n == 2:
    cnt_f = 1
else:
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    cnt_f = b

print(cnt_f, cnt_dp)
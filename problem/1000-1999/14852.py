n = int(input())  # 1 <= n <= 1_000_000
MOD = 1_000_000_007

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 2

acc = [0] * (n + 1)  # 누적합
acc[0] = 1
acc[1] = 3

for i in range(2, n + 1):
    dp[i] = dp[i - 1] * dp[1] + dp[i - 2]
    dp[i] %= MOD

    dp[i] += acc[i - 2] * 2
    dp[i] %= MOD

    acc[i] = acc[i - 1] + dp[i]
    acc[i] %= MOD

print(dp[n])

c, n = map(int, input().split())

dp = [float('inf')] * (c + 101)
dp[0] = 0

li = []

for _ in range(n):
    li.append(tuple(map(int, input().split())))

for cost, people in li:
    for i in range(people, c + 101):
        dp[i] = min(dp[i], dp[i - people] + cost)

print(min(dp[c:]))

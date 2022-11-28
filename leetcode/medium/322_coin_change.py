class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(amount + 1 - coin):
                if dp[i] == -1:
                    continue
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)

        return -1 if dp[-1] == float('inf') else dp[-1]

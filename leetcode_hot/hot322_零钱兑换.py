class Solution:
    def coinChange(self, coins, amount):
        dp = [10005] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i-coins[j]] + 1, dp[i])
        return dp[amount] if dp[amount] != 10005 else -1
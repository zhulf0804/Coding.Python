class Solution:
    def maxProfit(self, prices):
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = dp[i-1]
            for j in range(i):
                if prices[j] < prices[i]:
                    profit = prices[i] - prices[j]
                    if j - 2 >= 0:
                        profit += dp[j-2]
                    dp[i] = max(dp[i], profit)
        return dp[len(prices) - 1]
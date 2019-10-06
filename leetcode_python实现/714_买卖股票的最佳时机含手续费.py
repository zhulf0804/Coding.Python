from typing import List
class Solution_1:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0] - fee
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)
        return dp[n-1][0]

# 内存优化, 但提交结果显示并没有提升很多
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        dp = [0, 0]
        dp[1] = -prices[0] - fee
        for i in range(1, n):
            tmp1 = max(dp[0], dp[1] + prices[i])
            tmp2 = max(dp[1], dp[0] - prices[i] - fee)
            dp = [tmp1, tmp2]
        return dp[0]
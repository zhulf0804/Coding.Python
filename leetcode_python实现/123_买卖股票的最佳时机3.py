from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        dp[0][1][1] = -prices[0]
        dp[0][2][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, 3):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[n-1][2][0]

obj = Solution()
prices = [3,3,5,0,0,3,1,4]
obj.maxProfit(prices)
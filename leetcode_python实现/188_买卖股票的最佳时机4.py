from typing import List


class Solution_1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or len(prices) == 1 or k == 0:
            return 0
        n = len(prices)

        def helper(prices: List[int]) -> int:
            if not prices or len(prices) == 1:
                return 0
            n = len(prices)
            dp = [[0, 0] for _ in range(n)]
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            return dp[n - 1][0]

        if k > n // 2:
            return helper(prices)

        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        for i in range(1, k + 1):
            dp[0][i][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]

# 优化空间
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or len(prices) == 1 or k == 0:
            return 0
        n = len(prices)

        def helper(prices: List[int]) -> int:
            if not prices or len(prices) == 1:
                return 0
            n = len(prices)
            dp = [[0, 0] for _ in range(n)]
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            return dp[n - 1][0]

        if k > n // 2:
            return helper(prices)

        dp = [[0, 0] for _ in range(k + 1)]
        for i in range(1, k + 1):
            dp[i][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                tmp1 = max(dp[j][0], dp[j][1] + prices[i])
                tmp2 = max(dp[j][1], dp[j - 1][0] - prices[i])
                dp[j] = [tmp1, tmp2]
        return dp[k][0]

k = 2
prices = [2, 4, 1]
obj = Solution()
obj.maxProfit(k, prices)
from typing import List
## 超时
class Solution_1:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        dp = [0] * len(prices) # dp[i]表示最后一次是i位置卖出的最大利润
        dp[0] = 0
        dp[1] = prices[1] - prices[0]
        dp[2] = prices[2] - min(prices[0], prices[1])
        res = max(dp[0:3])
        for j in range(3, len(prices)):
            mmin = prices[j-1]
            for i in range(j - 3, -1, -1):
                mmin = min(prices[i+2], mmin)
                dp[j] = max(dp[j], dp[i] + prices[j] - mmin)
            dp[j] = max(dp[j], prices[j] - min([prices[0], prices[1], mmin]))
            if dp[j] > res:
                res = dp[j]
            #print(dp)
        return res

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][0] = 0
        dp[1][0] = max(0, prices[1] - prices[0])
        dp[1][1] = -min(prices[0], prices[1])
        for i in range(2, len(prices)):
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        return dp[len(prices) - 1][0]

prices = [6, 1, 3, 2, 4, 7]
obj = Solution()
res = obj.maxProfit(prices)
print(res)
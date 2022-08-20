class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        min_v = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_v)
            min_v = min(min_v, prices[i])
        return max_profit

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ans, mmin, n = 0, prices[0], len(prices)
        for i in range(1, n):
            ans = max(ans, prices[i] - mmin)
            mmin = min(mmin, prices[i])
        return ans
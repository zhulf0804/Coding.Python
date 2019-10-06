from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        mmin = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - mmin)
            mmin = min(mmin, prices[i])
        return res
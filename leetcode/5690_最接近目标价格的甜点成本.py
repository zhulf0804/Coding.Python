from typing import List

class Solution:
    def get_values(self, toppingCosts, base, values):
        if not toppingCosts:
            values.append(base)
            return
        for i in range(3):
            self.get_values(toppingCosts[1:], base + toppingCosts[0] * i, values)
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = float('inf')
        values = []
        self.get_values(toppingCosts, 0, values)
        for baseCost in baseCosts:
            for value in values:
                cur = baseCost + value
                if abs(cur - target) < abs(ans - target):
                    ans = cur
                elif abs(cur - target) == abs(ans - target):
                    if cur < ans:
                        ans = cur
        return ans
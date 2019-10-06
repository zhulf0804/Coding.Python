from typing import List
# 递归
class Solution_1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        counts = {}
        def helper(n):
            if n < 0:
                return -1
            if n == 0:
                return 0
            res = float('inf')
            for coin in coins:
                if n - coin in counts:
                    cost = counts[n-coin]
                else:
                    cost = helper(n - coin)
                    counts[n - coin] = cost
                if cost < 0:
                    continue
                res = min(res, 1 + cost)
            return -1 if res == float('inf') else res
        return helper(amount)

# 递推
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]
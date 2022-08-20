import math

class Solution:
    def numSquares(self, n):
        dp = [i for i in range(n+1)]
        for i in range(2, n+1):
            up = math.floor(math.sqrt(i))
            for j in range(1, up+1):
                dp[i] = min(dp[i - j * j] + 1, dp[i])
        return dp[n]
            

class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * max(i - j, dp[i - j]))
        return dp[n] % 1000000007
class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n <= 2:
            return n
        dp = [1, 2]
        m = int(1e9 + 7)
        for i in range(3, n+1):
            tmp = (dp[0] + dp[1]) % m
            dp[0] = dp[1]
            dp[1] = tmp
        return dp[1]

class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        # dp = [0] * (n + 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
        a, b = 1, 2
        i = 3
        while i <= n:
            tmp = b
            b = a + b
            a = tmp
            i += 1
        return b
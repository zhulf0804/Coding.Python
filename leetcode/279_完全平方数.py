class Solution:
    def numSquares(self, n: int) ->int:
        dp = [i for i in range(n+1)]
        for i in range(1, n + 1):
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        return dp[n]

n = 7168
s = Solution()
print(s.numSquares(n))
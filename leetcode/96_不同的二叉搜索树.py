class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j -1]
            #print(i, dp[i])
        return dp[n]

s = Solution()
res = s.numTrees(3)

print(res)
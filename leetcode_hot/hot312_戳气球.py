class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[0][n-1]
        dp = [[0] * n for _ in range(n)]
        for l in range(2, n):
            for i in range(n - l):
                # (i, i + l)
                for k in range(i+1, i+l):
                    dp[i][i+l] = max(dp[i][k] + dp[k][i+l] + nums[i] * nums[i+l] * nums[k], dp[i][i+l])
        return dp[0][n-1]
                
        

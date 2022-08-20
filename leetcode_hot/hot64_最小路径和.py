class Solution: 
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        dp = [0] * m
        for j in range(m):
            if j == 0:
                dp[j] = grid[0][j]
            else:
                dp[j] = dp[j-1] + grid[0][j]
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        return dp[m-1]
    
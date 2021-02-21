from typing import List

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        ans = -float('inf')
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i-1] + nums[n - i] * multipliers[i - 1]
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + nums[i - 1] * multipliers[i - 1]
        ans = max(ans, dp[0][m])
        ans = max(ans, dp[m][0])
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                if i + j > m:
                    continue
                dp[i][j] = max(dp[i-1][j] + nums[i - 1] * multipliers[i - 1 + j],
                               dp[i][j-1] + nums[n - j] * multipliers[i - 1 + j])
                if i + j == m:
                    ans = max(ans, dp[i][j])
        return ans
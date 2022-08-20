class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]
        return max(dp)
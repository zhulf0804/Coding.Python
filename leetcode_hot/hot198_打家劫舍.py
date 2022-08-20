class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
         
        dp = [0] * len(nums)
        dp[:2] = nums[:2]
        mmax = max(nums[:2])
        for i in range(2, len(nums)):
            if i == 2:
                dp[i] = nums[i] + dp[i-2]
            else:
                dp[i] = nums[i] + max(dp[i-2], dp[i-3])
            mmax = max(mmax, dp[i])
        return mmax

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_dp = [0] * len(nums)
        max_dp[0] = nums[0]
        min_dp = [0] * len(nums)
        min_dp[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i])
                min_dp[i] = min(nums[i], min_dp[i - 1] * nums[i])
            elif nums[i] < 0:
                max_dp[i] = max(nums[i], min_dp[i - 1] * nums[i])
                min_dp[i] = min(nums[i], max_dp[i - 1] * nums[i])
        return max(max_dp)

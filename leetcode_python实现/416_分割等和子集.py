from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [0] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, -1, -1):
                if dp[i] and i + num <= target:
                    dp[i + num] = True
        return dp[target]
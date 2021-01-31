from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mmax, dp = nums[0], nums[0]
        for i in range(1, len(nums)):
            if dp < 0:
                dp = nums[i]
            else:
                dp += nums[i]
            mmax = max(mmax, dp)
        return mmax
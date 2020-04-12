from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 3:
            return False
        mmin = nums[0]
        cmp = float('inf')
        for i in range(1, len(nums)):
            if nums[i] > cmp:
                return True
            if nums[i] > mmin:
                cmp = min(cmp, nums[i])
            mmin = min(mmin, nums[i])
        return False

nums = [0,4,2,1,0,-1,-3]
obj = Solution()
obj.increasingTriplet(nums)
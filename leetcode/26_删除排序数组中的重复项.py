from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        cur = 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 1
                continue
            nums[cur] = nums[i]
            i += 1
            cur += 1
        return cur

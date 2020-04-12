from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[(len(nums) - 1) // 2]

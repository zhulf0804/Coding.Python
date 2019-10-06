from typing import List
class Solution:
    def canJump(self, nums: List[int])  -> bool:
        left = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= left:
                left = i
        return True if left == 0 else False
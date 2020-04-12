from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                i += 1
                continue
            nums[cur] = nums[i]
            i += 1
            cur += 1
        return cur
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur = 0
        l = 0
        r = 1
        while r < len(nums):
            if nums[r] == nums[l]:
                r += 1
                continue
            length = r - l
            if length < 2:
                nums[cur] = nums[l]
                cur += 1
            else:
                nums[cur] = nums[l]
                nums[cur+1] = nums[l]
                cur += 2
            l = r
            r += 1
        length = r - l
        nums[cur] = nums[l]
        if length >= 2:
            cur += 1
            nums[cur] = nums[l]

        return cur + 1

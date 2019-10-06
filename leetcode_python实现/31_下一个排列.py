from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        for i in range(len(nums) - 2, -1, -1):
            loc = -1
            mmin = float('inf')
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i] and nums[j] < mmin:
                    loc = j
            if loc == -1:
                continue
            nums[loc], nums[i] = nums[i], nums[loc]
            nums[i+1:] = sorted(nums[i+1:])
            return
        nums = nums.reverse()

nums = [1, 2, 3]
s = Solution()
s.nextPermutation(nums)
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        my_nums = [0] * 3
        for num in nums:
            my_nums[num] += 1
        for i in range(len(nums)):
            if i < my_nums[0]:
                nums[i] = 0
            elif i < my_nums[0] + my_nums[1]:
                nums[i] = 1
            else:
                nums[i] = 2

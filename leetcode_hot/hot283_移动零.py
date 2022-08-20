# class Solution:
#     def moveZeroes(self, nums):
#         zero_num = 0
#         for num in nums:
#             if num == 0:
#                 zero_num += 1
#         i, j = 0, 0
#         while j < len(nums):
#             if nums[j] != 0:
#                 nums[i] = nums[j]
#                 i += 1
#             j += 1
#         for j in range(i, len(nums)):
#             nums[j] = 0

class Solution:
    def moveZeroes(self, nums):
        n = len(nums)
        i, j = 0, 0
        while i < n:
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        
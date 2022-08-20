# class Solution:
#     def sortColors(self, nums):
#         res_dict = {}
#         for num in nums:
#             res_dict[num] = res_dict.get(num, 0) + 1
#         i = 0
#         for num in [0, 1, 2]:
#             for j in range(res_dict.get(num, 0)):
#                 nums[i] = num
#                 i += 1

class Solution:
    def sortColors(self, nums):
        n = len(nums)
        i, k, j = 0, 0, n - 1
        while k <= j:
            if nums[k] < 1:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            elif nums[k] == 1:
                k += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
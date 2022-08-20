# class Solution:
#     def longestConsecutive(self, nums):
#         nums = set(nums)
#         res = 0
#         for num in nums:
#             if num - 1 not in nums:
#                 count = 1
#                 while num + 1 in nums:
#                     count += 1
#                     num += 1
#                 res = max(res, count)
#         return res


class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        res = 0
        dict = {}
        for num in nums:
            if num not in dict:
                count = 1
                tmp_num = num
                dict[tmp_num] = 1
                while tmp_num + 1 in nums:
                    count += 1
                    tmp_num += 1
                    dict[tmp_num] = 1
                tmp_num = num
                while tmp_num - 1 in nums:
                    count += 1
                    tmp_num -= 1
                    dict[tmp_num] = 1
                res = max(res, count)
        return res
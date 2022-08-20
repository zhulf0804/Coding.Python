# class Solution:
#     def twoSum(self, nums, target):
#         d = {}
#         for i, num in enumerate(nums):
#             if num in d:
#                 d[num] += [i]
#             else:
#                 d[num] = [i]
#         nums = list(sorted(nums))
#         i, j = 0, len(nums) - 1
#         while i < j:
#             if nums[i] + nums[j] == target:
#                 if nums[i] == nums[j]:
#                     return d[nums[i]]
#                 else:
#                     return d[nums[i]] + d[nums[j]]
#             if nums[i] + nums[j] < target:
#                 i += 1
#             else:
#                 j -= 1


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for i, num in enumerate(nums):
            j = hashmap.get(target-num, -1)
            if j != -1 and j != i:
                return [i, j]
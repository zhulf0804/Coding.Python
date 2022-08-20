# class Solution:
#     def search(self, nums, target):
#         n = len(nums)
#         l, r = 0, n - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             first = nums[mid] >= nums[0]
            
#             if first:
#                 if nums[mid] < target:
#                     l = mid + 1
#                 else:
#                     if target == nums[0]:
#                         return 0
#                     if target > nums[0]:
#                         r = mid - 1
#                     else:
#                         l = mid + 1
#             else:
#                 if nums[mid] > target:
#                     r = mid - 1
#                 else:
#                     if target == nums[-1]:
#                         return n - 1
#                     if nums[-1] > target:
#                         l = mid + 1
#                     else:
#                         r = mid - 1
#         return -1

class Solution:
    def search(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0] and (target > nums[mid] or target < nums[0]):
                l = mid + 1
            elif nums[mid] < nums[0] and target > nums[mid] and target <= nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
            
        return -1
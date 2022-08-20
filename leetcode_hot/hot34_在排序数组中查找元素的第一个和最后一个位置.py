# class Solution:
#     def searchRange(self, nums, target):
#         n = len(nums)
#         if n == 0:
#             return [-1, -1]
#         l, r = 0, n - 1
#         while l < r:
#             mid = (l + r) // 2
#             if nums[mid] <= target:
#                 l = mid + 1
#             else:
#                 r = mid
        
#         if nums[l] < target:
#             return [-1, -1]
#         if nums[l] == target:
#             res = [l]
#         else:
#             if l == 0:
#                 return [-1, -1]
#             if nums[l-1] != target:
#                 return [-1, -1] 
#             res = [l - 1]

#         l, r = 0, n - 1
#         while l < r:
#             mid = (l + r + 1) // 2
#             if nums[mid] >= target:
#                 r = mid - 1
#             else:
#                 l = mid
#         if nums[l] == target:
#             return [l] + res
#         else:
#             return [l + 1] + res
        

class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] != target:
            return [-1, -1]
        
        res = [l]
        l, r = 0, n - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        
        return res + [l]
            
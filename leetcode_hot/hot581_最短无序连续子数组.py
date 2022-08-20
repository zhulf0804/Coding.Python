# class Solution:
#     def findUnsortedSubarray(self, nums):
#         n = len(nums)
#         left, right = n, n
#         for i in range(1, n):
#             for j in range(i):
#                 if nums[j] > nums[i]:
#                     left = min(left, j)
#                     right = i
#                     break
#         if left == n:
#             return 0 
#         return right - left + 1

class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        right, mmax = -1, nums[0]
        for i in range(1, n):
            if nums[i] < mmax:
                right = i
            mmax = max(mmax, nums[i])
        
        left, mmin = n, nums[-1]
        for i in range(n-2, -1, -1):
            if nums[i] > mmin:
                left = i
            mmin = min(mmin, nums[i])
        if right == -1:
            return 0
        return right - left + 1
        
# class Solution:
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         left = [1] * (n + 1)
#         for i in range(1, n + 1):
#             left[i] = left[i-1] * nums[i-1]
#         right = [1] * (n + 1)
#         for i in range(1, n + 1):
#             right[i] = right[i-1] * nums[n-i]

#         res = []
#         for i in range(n):
#             ans = left[i] * right[n - 1 - i]
#             res.append(ans)
#         return res 

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        tmp = nums[-1]
        for i in range(n-2, -1, -1):
            res[i] *= tmp 
            tmp *= nums[i]
        return res

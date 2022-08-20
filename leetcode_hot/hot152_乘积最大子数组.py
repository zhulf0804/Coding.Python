class Solution:
    def maxProduct(self, nums):
        dpmax, dpmin = [0] * len(nums), [0] * len(nums)
        dpmax[0], dpmin[0] = nums[0], nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            vals = [nums[i], nums[i] * dpmax[i-1], nums[i] * dpmin[i-1]]
            dpmax[i] = max(vals)
            dpmin[i] = min(vals)
            ans = max(ans, dpmax[i])
        return ans
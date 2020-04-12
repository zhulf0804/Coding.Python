from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_max = -1
        res = nums[0]
        for num in nums:
            cur_max = num + max(0, pre_max)
            res = max(cur_max, res)
            pre_max = cur_max
        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
res = s.maxSubArray(nums)
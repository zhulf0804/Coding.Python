from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, cur):
            if not nums:
                if len(cur) >= 2:
                    res.append(cur)
                return
            if not cur:
                helper(nums[1:], cur + [nums[0]])
                helper(nums[1:], cur)
            else:
                if nums[0] >= cur[-1]:
                    helper(nums[1:], cur + [nums[0]])
                helper(nums[1:], cur)
        helper(nums, [])
        return list(set(tuple(t) for t in res))

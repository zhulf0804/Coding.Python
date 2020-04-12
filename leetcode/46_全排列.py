from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, cur_val):
            if not nums:
                res.append(cur_val)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], cur_val + [nums[i]])
        backtrack(nums, [])
        return res

nums = [1, 2, 3]

s = Solution()
res = s.permute(nums)
print(res)
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res_sum = nums[0] + nums[1] + nums[2]
        res = abs(res_sum - target)
        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                ssum = num + nums[l] + nums[r]
                if ssum == target:
                    return ssum
                if abs(target - ssum) < res:
                    res = abs(target - ssum)
                    res_sum = ssum
                if ssum > target:
                    r -= 1
                else:
                    l += 1
        return res_sum

nums = [-1,2,1,-4]
target = 1
s = Solution()
print(s.threeSumClosest(nums, target))
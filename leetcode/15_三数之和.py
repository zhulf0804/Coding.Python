from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        i = 0
        while i < len(nums)-2:
            if nums[i] > 0:
                break
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while r > l:
                if nums[l] + nums[r] == target:
                    results.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    continue
                if nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i - 1]:
                i += 1
        return results

s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
res = s.threeSum(nums)
print(res)

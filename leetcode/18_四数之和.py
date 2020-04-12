from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        length = len(nums)
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = length - 1
                while l < r:
                    summ = nums[i] + nums[j] + nums[l] + nums[r]
                    if summ == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        r -= 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif summ < target:
                        l += 1
                    else:
                        r -= 1
        return res

nums = [-3,-2,-1,0,0,1,2,3]
target = 0
s = Solution()
print(s.fourSum(nums, target))
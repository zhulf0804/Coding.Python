from typing import List

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums[0] != 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i+1] != nums[i] + 1:
                return nums[i] + 1
        return nums[-1] + 1
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid
        # 若全部相等，则返回n-1
        if nums[l] == l:
            return nums[-1] + 1
        return nums[l] - 1
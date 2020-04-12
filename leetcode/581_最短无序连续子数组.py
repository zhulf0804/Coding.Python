from typing import List

# sorted
class Solution_1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        l = 0
        r = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                l = i
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sorted_nums[i]:
                r = i
                break
        return r - l + 1

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        maxIndex = 0
        l, r = None, 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[maxIndex]:
                maxIndex = i
            else:
                r = i
                if l == None:
                    l = i - 1
                while l > 0 and nums[l-1] > nums[r]:
                    l -= 1
        return r - l + 1 if l is not None else 0


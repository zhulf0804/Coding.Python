from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0] and (target > nums[mid] or target < nums[0]):
                l = mid + 1
            elif nums[mid] < nums[0] and target > nums[mid] and target < nums[0]:
                l = mid + 1
            else:
                r = mid
        return l if nums[l] == target else -1





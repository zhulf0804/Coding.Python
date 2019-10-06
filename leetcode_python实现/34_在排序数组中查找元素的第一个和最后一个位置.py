from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        ## 寻找第一个等于target的值
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
        if nums[l] != target:
            return res
        res[0] = l
        ## 寻找第一个大于target的值或最后一个大于target的值
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid]  > target:
                r = mid
            elif nums[mid] <= target:
                l = mid + 1
        res[1] = l - 1 if nums[l] > target else l
        return res

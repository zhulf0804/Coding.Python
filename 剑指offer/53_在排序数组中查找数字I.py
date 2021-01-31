from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        l ,r = 0, n - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid
        if nums[l] >= target:
            l -= 1

        l2, r2 = 0, n - 1
        while l2 < r2:
            mid = l2 + (r2 - l2) // 2
            if nums[mid] <= target:
                l2 = mid + 1
            else:
                r2 = mid
        if nums[l2] <= target:
            l2 += 1

        return l2 - l - 1
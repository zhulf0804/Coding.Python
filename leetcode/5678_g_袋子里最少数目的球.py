from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, int(1e9 + 5)
        while l < r:
            mid = l + (r - l) // 2
            ans = 0
            for num in nums:
                ans += (num - 1) // mid
            if ans > maxOperations:
                l = mid + 1
            else:
                r = mid
        return l

nums = [431,922,158,60,192,14,788,146,788,775,772,792,68,143,376,375,877,516,595,82,56,704,160,403,713,504,67,332,26]
maxOperations = 80

a = Solution()
print(a.minimumSize(nums, maxOperations))
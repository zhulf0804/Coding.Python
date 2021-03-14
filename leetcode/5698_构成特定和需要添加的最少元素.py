from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(sum(nums) - goal)
        ans = diff // limit
        if diff % limit != 0:
            ans += 1
        return ans

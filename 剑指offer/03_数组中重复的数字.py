from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                return num
            d[num] = 1

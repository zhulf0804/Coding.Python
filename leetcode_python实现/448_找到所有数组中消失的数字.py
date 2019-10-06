from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for i in range(1, len(nums) + 1):
            if i not in d:
                res.append(i)
        return res
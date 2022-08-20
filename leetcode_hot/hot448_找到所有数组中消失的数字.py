from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            index = num % n - 1
            nums[index] += n
        
        res = []
        for i, num in enumerate(nums):
            if num <= n:
                res.append(i+1)
        return res

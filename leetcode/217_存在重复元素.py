from typing import List
# 暴力、排序、哈希
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) - len(set(nums))
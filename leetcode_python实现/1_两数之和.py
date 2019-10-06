from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            another_num = target - num
            if hashmap.get(another_num) is not None:
                return [hashmap.get(another_num), i]
            hashmap[num] = i


a = Solution()

nums = [2, 7, 11, 15]
target = 9
res = a.twoSum(nums, target)

print(res)
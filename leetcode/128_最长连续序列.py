from typing import List
from queue import PriorityQueue
# 优先队列
class Solution_1:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        q = PriorityQueue()
        for num in nums:
            d[num] = 1
            q.put(num)
        while q.qsize() > 0:
            val = q.get()
            d[val] = d.get(val-1, 0) + 1
        res = 0
        for key, val in d.items():
            if val > res:
                res = val
        return res

# 排序
class Solution_2:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res, count = 1, 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i += 1
                continue
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                res = max(count, res)
                count = 1
            i += 1
        res = max(count, res)
        return res

## 哈希

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        res = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                count = 1
                while num + 1 in nums_set:
                    num += 1
                    count += 1
                res = max(count, res)
        return res




nums = [0, -1]
obj = Solution()
print(obj.longestConsecutive(nums))
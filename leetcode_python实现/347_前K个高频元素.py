from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        res = heapq.nlargest(k, d, key=lambda x: d[x])
        #d = sorted(d, key=lambda x:d[x])
        return res

nums = [1,1,1,2,3,3, 3, 4,2,3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))
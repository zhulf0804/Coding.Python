from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        if k == 1:
            return nums

        def helper(i):
            if i - deq[0] >= k:
                deq.popleft()
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)

        deq = deque()
        # init
        deq.append(0)
        for i in range(1, k):
            helper(i)

        res = [nums[deq[0]]]
        for i in range(k, len(nums)):
            helper(i)
            res.append(nums[deq[0]])
        return res

nums = [1, 3, 1, 2, 0, 5]
k = 3
obj = Solution()
print(obj.maxSlidingWindow(nums, k))



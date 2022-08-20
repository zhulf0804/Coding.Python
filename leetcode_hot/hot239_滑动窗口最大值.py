from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        q = deque()
        l, r = 0, 0
        res = []
        while r < n:
            while len(q) > 0 and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            if r - l + 1 == k:
                l += 1
                res.append(nums[q[0]])
                if q[0] < l:
                    q.popleft()
            r += 1
        return res
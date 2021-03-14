from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        size = len(nums)
        res = 0

        stack = []

        for i in range(size):
            while len(stack) > 0 and nums[i] < nums[stack[-1]]:
                right = i - 1
                cur_height = nums[stack.pop()]

                while len(stack) > 0 and cur_height == nums[stack[-1]]:
                    stack.pop()

                if len(stack) > 0:
                    left = stack[-1] + 1
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i
                    left = 0
                if left <= k and right >= k:
                    res = max(res, cur_height * cur_width)
            stack.append(i)

        while len(stack) > 0 is not None:
            cur_height = nums[stack.pop()]
            while len(stack) > 0 and cur_height == nums[stack[-1]]:
                stack.pop()
            right = size - 1
            if len(stack) > 0:
                cur_width = size - stack[-1] - 1
                left = stack[-1] + 1
            else:
                cur_width = size
                left = 0
            if left <= k and right >= k:
                res = max(res, cur_height * cur_width)

        return res

from typing import List

# 超时
class Solution_1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        mmin = float('inf')
        for i in range(len(nums)):
            summ = nums[i]
            if summ >= s:
                return 1
            for j in range(i+1, len(nums)):
                summ += nums[j]
                if summ >= s:
                    mmin = min(j - i + 1, mmin)
        return mmin if mmin < float('inf') else 0


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        mmin = float('inf')
        summ = [0] * len(nums)
        summ[0] = nums[0]
        for i in range(1, len(nums)):
            summ[i] = summ[i - 1] + nums[i]

        for i in range(len(nums)):
            l = i
            r = len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                tmp_sum = summ[mid] - summ[i] + nums[i]
                if tmp_sum < s:
                    l = mid + 1
                else:
                    r = mid
            if summ[l] - summ[i] + nums[i] < s:
                continue
            else:
                mmin = min(mmin, l - i + 1)
        return mmin if mmin < float('inf') else 0

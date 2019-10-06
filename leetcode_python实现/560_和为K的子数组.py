from typing import List
# 超时
class Solution_1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ = [0] * len(nums)
        summ[0] = nums[0]
        for i in range(1, len(nums)):
            summ[i] = summ[i - 1] + nums[i]

        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
               if summ[j] - summ[i] + nums[i] == k:
                   res += 1
        return res

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict = {0:1}
        res = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            res += dict.get(summ - k, 0)
            dict[summ] = dict.get(summ, 0) + 1
        return res

nums = [1, 1, 1]
k = 2
s = Solution()
print(s.subarraySum(nums, k))
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans, base = 0, 0
        for j in range(32):
            summ = 0
            for i in range(len(nums)):
                if nums[i] & 1 == 1:
                    summ += 1
                if j != 31:
                    nums[i] = nums[i] >> 1
            if summ % 3 == 1:
                ans += pow(2, base)
            base += 1
        return ans
'''
1 <= nums.length <= 10000
1 <= nums[i] < 2^31
'''
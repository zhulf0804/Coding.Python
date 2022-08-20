class Solution:
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans
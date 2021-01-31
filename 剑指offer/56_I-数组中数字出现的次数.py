from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        a = 0
        for num in nums:
            a ^= num
        b = a - (a & (a - 1))
        arra, arrb = [], []
        for num in nums:
            if b & num == 0:
                arra.append(num)
            else:
                arrb.append(num)
        ansa, ansb = 0, 0
        for num in arra:
            ansa ^= num
        for num in arrb:
            ansb ^= num
        return [ansa, ansb]

nums = [4,1,4,6]
a = Solution()
print(a.singleNumbers(nums))
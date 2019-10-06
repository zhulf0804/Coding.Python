from typing import List
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def mycmp(num1, num2):
            num1, num2 = str(num1), str(num2)
            if num1 + num2 > num2 + num1:
                return 1
            elif num1 + num2 == num2 + num1:
                return 0
            else:
                return -1

        nums = sorted(nums, key=cmp_to_key(lambda x, y: mycmp(x, y)), reverse=True)
        nums = [str(num) for num in nums]
        return ''.join(nums)

nums = [3,30,34,9, 5]
s = Solution()
print(s.largestNumber(nums))
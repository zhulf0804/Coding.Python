from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number, ans = 0, nums[0]
        for num in nums:
            if number == 0:
                ans = num
                number += 1
            else:
                if num == ans:
                    number += 1
                else:
                    number -= 1
        return ans

from typing import List

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        zero_num = 0
        for num in nums:
            if num != 0:
                break
            zero_num += 1
        for i in range(zero_num, 4):
            if nums[i] == nums[i+1]:
                return False
            if nums[i] + 1 == nums[i+1]:
                continue
            else:
                while zero_num > 0:
                    zero_num -= 1
                    nums[i] += 1
                    if nums[i] + 1 == nums[i+1]:
                        break
                if nums[i] + 1 != nums[i+1]:
                    return False
        return True

nums = [11,0,9,0,0]
a = Solution()
print(a.isStraight(nums))
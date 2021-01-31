from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        while j >= 0:
            if nums[j] % 2 == 1:
                break
            j -= 1
        while i < j:
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                continue
            j -= 1
            while j >= 0:
                if nums[j] % 2 == 1:
                    break
                j -= 1
            i += 1
        return nums

a = Solution()
nums = [2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]
print(a.exchange(nums))
print([3,5,13,1,1,11,11,11,5,1,2,16,16,12,18,8])
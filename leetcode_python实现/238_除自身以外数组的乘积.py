from typing import List
## 代码不美观
class Solution_1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        res = [1] * len(nums)
        mul_left = [1] * len(nums)
        mul_right = [1] * len(nums)
        mul_left[0] = nums[0]
        mul_right[-1] = nums[-1]
        for i in range(1, len(nums)):
            mul_left[i] = mul_left[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            mul_right[i] = mul_right[i + 1] * nums[i]
        for i in range(len(nums)):
            if i == 0:
                res[i] = mul_right[1]
            elif i == len(nums) - 1:
                res[i] = mul_left[-2]
            else:
                res[i] = mul_left[i-1] * mul_right[i + 1]
        return res

## 优化的代码
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for num in nums[:-1]:
            prefix.append(prefix[-1] * num)
        suffix = [1]
        for num in nums[::-1][:-1]:
            suffix.append(suffix[-1] * num)

        return list([a * b for a, b in zip(prefix, suffix[::-1])])


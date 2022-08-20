class Solution:
    def majorityElement(self, nums):
        ans = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                ans = nums[i]
                count += 1
                continue
            if nums[i] == ans:
                count += 1
            else:
                count -= 1
        return ans

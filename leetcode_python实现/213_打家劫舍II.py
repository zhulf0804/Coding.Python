from typing import List
class Solution_1:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def helper(nums):
            if not nums:
                return 0
            if len(nums) <= 2:
                return max(nums)
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[len(nums) - 1]
        n = len(nums)
        return max(nums[n-1] + helper(nums[1:n-2]), helper(nums[:n-1]))

## 节省内存的算法
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        def helper(nums):
            pre, cur = 0, 0
            for num in nums:
                tmp = max(num + pre, cur)
                pre = cur
                cur = tmp
            return cur
        n = len(nums)
        return max(nums[n - 1] + helper(nums[1:n - 2]), helper(nums[:n - 1]))


nums = [4,1,2,7,5,3,1]
obj = Solution()
print(obj.rob(nums))
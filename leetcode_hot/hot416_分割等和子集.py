# class Solution:
#     def canPartition(self, nums):
#         summ = sum(nums)
#         if summ % 2 == 1:
#             return False
#         target = summ // 2
#         def helper(nums, target):
#             if target == 0:
#                 return True
#             if len(nums) == 0:
#                 return False
#             for i in range(len(nums)):
#                 exist = helper(nums[:i] + nums[i+1:], target-nums[i])
#                 if exist:
#                     return True
#             return False
#         return helper(nums, target)

# class Solution:
#     def canPartition(self, nums):
#         summ = sum(nums)
#         if summ % 2 == 1:
#             return False
#         target = summ // 2
#         dp = [0] * (target + 1)
#         dp[0] = 1
#         for num in nums:
#             for i in range(target, -1, -1):
#                 if dp[i] and i + num <= target:
#                     dp[i+num] = 1
#         return bool(dp[target])


# class Solution:
#     def canPartition(self, nums):
#         summ = sum(nums)
#         if summ % 2 == 1:
#             return False
#         target = summ // 2
#         n = len(nums)
#         dp = [[0] * (target + 1) for _ in range(n)]
#         if nums[0] <= target:
#             dp[0][nums[0]] = 1
#         dp[0][0] = 1
#         for i in range(1, n):
#             for j in range(target+1):
#                 dp[i][j] = dp[i-1][j]
#                 if nums[i] <= j:
#                     dp[i][j] = dp[i-1][j-nums[i]] or dp[i][j]

#         return bool(dp[n-1][target])

class Solution:
    def canPartition(self, nums):
        summ = sum(nums)
        if summ % 2 == 1:
            return False
        target = summ // 2
        n = len(nums)
        dp = [0] * (target + 1)
        if nums[0] <= target:
            dp[nums[0]] = 1
        dp[0] = 1
        for i in range(1, n):
            for j in range(target, -1, -1):
                if nums[i] <= j:
                    dp[j] = dp[j-nums[i]] or dp[j]

        return bool(dp[target])
from typing import List

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         # dp[i][v] = dp[i-1][v-nums[i]] + dp[i-1][v+nums[i]]
#         # i=0, ..., n-1
#         # v=
#         # return dp[n-1][target]
#         n = len(nums)
#         summ = sum(nums)
#         if abs(summ) < abs(target):
#             return 0
#         dp = [[0] * (2 * summ + 1) for _ in range(n)]
#         dp[0][summ - nums[0]] += 1
#         dp[0][summ + nums[0]] += 1
#         for i in range(1, n):
#             for v in range(2*summ + 1):
#                 if v - nums[i] >= 0:
#                     dp[i][v] += dp[i-1][v-nums[i]]
#                 if v + nums[i] < 2 * summ + 1:
#                     dp[i][v] += dp[i-1][v+nums[i]]
        
#         return dp[n-1][summ + target]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        summ = sum(nums)
        target = target + summ
        if target % 2 != 0 or target < 0:
            return 0
        target = target // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for v in range(target, -1, -1):
                if v - nums[i] >= 0:
                    dp[v] += dp[v-nums[i]]
        return dp[target]


s = Solution()
ans = s.findTargetSumWays([1,1,1,1,1], 3)
print(ans)

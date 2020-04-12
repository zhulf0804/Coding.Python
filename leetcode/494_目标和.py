from typing import List

# 枚举法, 超时
class Solution_1:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.res = 0
        def get_list(length, cur):
            if length == 0:
                if sum([a * b for a, b in zip(cur, nums)]) == S:
                    self.res += 1
                return
            get_list(length-1, cur + [1])
            get_list(length-1, cur + [-1])
        get_list(len(nums), [])
        return self.res

# 0, 1背包
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        target = sum(nums) + S
        if target % 2 != 0:
            return 0
        target = target // 2
        if target > sum(nums):
            return 0
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] += dp[i-num]
            print(dp)
        return dp[target]

nums = [1,2,7,9,981]
S = 1000000000
s = Solution()
print(s.findTargetSumWays(nums, S))
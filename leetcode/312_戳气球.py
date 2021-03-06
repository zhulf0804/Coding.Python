from typing import List

# 暴力法 超时 (通过 13/70 个测试用例)
class Solution_1:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums
        nums.append(1)
        def helper(lst):
            if len(lst) == 3:
                return lst[1]
            mmax = 0
            for i in range(1, len(lst)  - 1):
                tmp = lst[i-1] * lst[i] * lst[i+1]
                mmax = max(mmax, tmp + helper(lst[:i] + lst[i+1:]))
            return mmax
        return helper(nums)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for step in range(2, n):
            for i in range(n):
                if step == 2:
                    if i + step < n:
                        dp[i][i+step] = nums[i] * nums[i+1] * nums[i+2]
                        #print(i, i + step, dp[i][i+step])
                    continue
                for k in range(i+1, i+step):
                    if i + step < n:
                        dp[i][i+step] = max(dp[i][k] + dp[k][i+step] + nums[i] * nums[k] * nums[i+step], dp[i][i+step])
                        #print(i, i + step, dp[i][i+step])
        return dp[0][n-1]


nums = [3, 1, 5, 8]
obj = Solution()
print(obj.maxCoins(nums))
# class Solution:
#     def lengthOfLIS(self, nums):
#         n = len(nums)
#         dp = [1] * n
#         mmax = 1
#         for i in range(1, n):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#             mmax = max(mmax, dp[i])
#         return mmax

class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        tails[0] = nums[0]
        ans = 1
        for i in range(1, len(nums)):
            l, r = 0, ans - 1
            while l < r:
                mid = (l + r) // 2
                if tails[mid] < nums[i]:
                    l = mid + 1
                else:
                    r = mid
            if tails[l] >= nums[i]:
                tails[l] = nums[i]
            else:
                ans += 1
                tails[ans-1] = nums[i]
        return ans

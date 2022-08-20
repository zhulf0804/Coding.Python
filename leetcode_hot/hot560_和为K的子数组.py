# class Solution:
#     def subarraySum(self, nums, k):
#         n = len(nums)
#         summ = [nums[0]]
#         for i in range(1, n):
#             summ.append(summ[-1] + nums[i])
        
#         ans = 0
#         for i in range(n):
#             for j in range(i, n):
#                 cur_sum = summ[j] - summ[i] + nums[i]
#                 if cur_sum == k:
#                     ans += 1
        
#         return ans

class Solution:
    def subarraySum(self, nums, k):
        pre_sum = {0:1}
        summ = 0
        ans = 0
        for num in nums:
            summ += num
            if summ - k in pre_sum:
                ans += pre_sum[summ - k]
            pre_sum[summ] = pre_sum.get(summ, 0) + 1
        return ans


'''
寻找两个有序数组的逆序对，写的不熟练
'''

from typing import List

class Solution:
    def helper(self, nums, l, r):
        if l >= r:
            return 0

        # child problem
        m = (l + r) // 2
        ans = self.helper(nums, l, m)
        ans += self.helper(nums, m+1, r)
        i, j = l, m + 1
        hi, hj = m, r
        while i <= hi:
            if j > hj:
                ans += (j - m - 1) * (hi - i + 1)
                break
            if nums[i] <= nums[j]:
                ans += (j - m - 1)
                i += 1
            else:
                while j <= hj and nums[i] > nums[j]:
                    j += 1
                ans += (j - m - 1)
                i += 1

        # sort
        tmp = []
        i, j = l, m + 1
        while i <= hi and j <= hj:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        while i <= hi:
            tmp.append(nums[i])
            i += 1
        while j <= hj:
            tmp.append(nums[j])
            j += 1
        for i in range(l, r + 1):
            nums[i] = tmp[i-l]
        return ans

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = self.helper(nums, 0, n-1)
        return ans


nums = [1,3,2,3,1]
a = Solution()
print(a.reversePairs(nums))
print(nums)

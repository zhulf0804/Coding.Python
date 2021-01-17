from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                cur = nums[i] * nums[j]
                d[cur] = d.get(cur, 0) + 1
        ans = 0
        for k, v in d.items():
            if v == 1:
                continue
            cur = v * (v - 1) * 4
            ans += cur
        return ans

a = Solution()
nums = [2,3,5,7]
print(a.tupleSameProduct(nums))
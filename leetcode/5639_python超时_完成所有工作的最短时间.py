from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        tot = [0] * (1 << n)
        for i in range(1, 1 << n):
            for j in range(n):
                if i & (1 << j) == 0:
                    continue
                tot[i] = jobs[j] + tot[i - (1 << j)]
                break
        mmax, summ = 0, 0
        for item in jobs:
            mmax = max(mmax, item)
            summ += item
        l, r = mmax, summ
        while l < r:
            mid = (l + r) // 2
            dp = [float('inf')] * (1 << n)
            dp[0] = 0
            for i in range(1, 1 << n):
                s = i
                while s:
                    if tot[s] <= mid:
                        dp[i] = min(dp[i], dp[i - s] + 1)
                    s = (s - 1) & i
            if dp[(1 << n) - 1] <= k:
                r = mid
            else:
                l = mid + 1
        return l

jobs = [256,250,255,250,254,255,260,260,250,252,257,253]
k = 9
a = Solution()
print(a.minimumTimeRequired(jobs, k))
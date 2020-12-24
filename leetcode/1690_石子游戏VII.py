from typing import List
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        summ, cur = [0], 0
        for item in stones:
            cur += item
            summ.append(cur)
        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(summ[j+1] - summ[i+1] - dp[i+1][j],
                               summ[j]- summ[i] - dp[i][j-1])
        return dp[0][n-1]

a = Solution()
stones = [7,90,5,1,100,10,10,2]
print(a.stoneGameVII(stones=stones))
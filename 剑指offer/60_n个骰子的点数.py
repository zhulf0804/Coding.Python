from typing import List

'''
递归超时
class Solution:
    def helper(self, n, summ, d):
        if n == 0:
            d[summ] = d.get(summ, 0) + 1
            return
        for i in range(1, 7):
            self.helper(n-1, i + summ, d)
    def dicesProbability(self, n: int) -> List[float]:
        d = {}
        self.helper(n, 0, d)
        keys = sorted(d.keys())
        res = []
        for key in keys:
            cur = d[key] / pow(6, n)
            res.append(cur)
        return res
'''

class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        mmax = n * 6
        dp = [[0] * (mmax + 1) for _ in range(n)]
        for j in range(1, 7):
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, mmax+1):
                for k in range(1, 7):
                    if k < j and j - k >= i:
                        dp[i][j] += dp[i-1][j-k]
        res = []
        for j in range(n, 6*n+1):
            res.append(dp[n-1][j] / pow(6, n))
        return res

a = Solution()
print(a.dicesProbability(2))
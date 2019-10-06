# 超时
class Solution_1:
    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True
        dp = [0] * (n + 1)
        dp[0:4] = [1, 1, 1, 1]
        for i in range(4, n + 1):
            #print(i, dp)
            dp[i] = not dp[i-1] or not dp[i-2] or not dp[i-3]

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4

n = 4
s = Solution()
print(s.canWinNim(n))
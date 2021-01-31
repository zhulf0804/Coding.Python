class Solution:
    def translateNum(self, num: int) -> int:
        n = len(str(num))
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        tmp = int(str(num)[0]) * 10 + int(str(num)[1])
        if tmp >= 10 and tmp <= 25:
            dp[1] = 2
        else:
            dp[1] = 1
        for i in range(2, n):
            dp[i] += dp[i-1]
            tmp = int(str(num)[i-1]) * 10 + int(str(num)[i])
            if tmp >= 10 and tmp <= 25:
                dp[i] += dp[i-2]
        return dp[n-1]

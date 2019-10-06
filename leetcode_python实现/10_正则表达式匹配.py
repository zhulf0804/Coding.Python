class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = 1
        for j in range(n-1, -1, -1):
            if j + 1 < n and p[j+1] == '*':
                dp[m][j] = dp[m][j+2]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                #print(i, j)
                if p[j] == '*':
                    continue
                if p[j] in [s[i], '.']:
                    if j + 1 < n and p[j+1] == '*':
                        dp[i][j] = dp[i+1][j] or dp[i][j+2]
                    else:
                        dp[i][j] = dp[i+1][j+1]
                elif j + 1 < n and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2]
        return dp[0][0]




obj = Solution()
s = "aab"
p = "c*a*b"
print(obj.isMatch(s, p))






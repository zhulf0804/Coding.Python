class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1

        for i in range(n-2, -1, -1):
            for j in range(i+2, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]

        for i in range(n-2):
            for j in range(i+1, n-1):
                if dp[0][i] == 1 and dp[i+1][j] == 1 and dp[j+1][n-1] == 1:
                    return True

        return False
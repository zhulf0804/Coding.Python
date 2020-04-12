class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s) - 1 and s[i] == s[i+1]:
                dp[i][i+1] = 1

        for l in range(2, len(s)):
            for i in range(len(s)):
                if i + l < len(s) and s[i] == s[i+l] and dp[i+1][i + l - 1]:
                    dp[i][i+l] = 1

        return sum(map(sum, dp))
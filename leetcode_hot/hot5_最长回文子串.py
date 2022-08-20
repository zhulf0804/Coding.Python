class Solution:
    def longestPalindrome(self, s):
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        mmax, res = 1, [0, 0]

        for l in range(2, len(s) + 1):
            for i in range(len(s) - l + 1):
                if s[i] == s[i+l-1]:
                    if l == 2:
                        dp[i][i+l-1] = 1
                    if l > 2 and dp[i + 1][i+l-2]:
                        dp[i][i+l-1] = 1
                if dp[i][i+l-1] and l > mmax:
                    mmax = l
                    res = [i, i+l-1]
        return s[res[0]:res[1]+1]

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        word = word1 + word2
        nm = n + m
        dp = [[1] * (nm) for _ in range(nm)]
        ans = 0
        for i in range(1, nm - 1):
            if word[i] == word[i+1]:
                if i == n - 1:
                    ans = 2
                dp[i][i+1] = 2

        for i in range(nm - 2, -1, -1):
            for j in range(i+2, nm):
                if word[i] == word[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                    if i < n and j >= n:
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return ans

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(n):
            dp[m][i] = n - i
        for i in range(m):
            dp[i][n] = m - i
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min([dp[i][j+1], dp[i+1][j+1], dp[i+1][j]]) + 1
                #print(i, j, dp[i][j])
        return dp[0][0]

word1 = "horse"
word2 = "ros"
obj = Solution()
print(obj.minDistance(word1, word2))
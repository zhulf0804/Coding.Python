# n x m
# 状态 dp[i][j]: word1[i:] 转换成 word2[j:]所使用的最少操作数
# 求dp[0][0]
# dp[i][j] = 
#            dp[i+1][j+1]   if word1[i] == word2[j]
#            min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j]) + 1
# init: dp[n-1][:] = 
#       dp[:][m-1] = 

class Solution:
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)

        if n == 0:
            return m
        if m == 0:
            return n

        dp = [[0] * m for _ in range(n)]
        
        # init
        if word1[n-1] != word2[m-1]:
            dp[n-1][m-1] = 1
        for j in range(m-2, -1, -1):
            if word1[n-1] == word2[j]:
                dp[n-1][j] = m - j - 1
            else:
                dp[n-1][j] = 1 + dp[n-1][j+1] 
        for i in range(n-2, -1, -1):
            if word1[i] == word2[m-1]:
                dp[i][m-1] = n - i - 1
            else:
                dp[i][m-1] = 1 + dp[i+1][m-1]
        
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j]) + 1
        
        return dp[0][0]

# n x m
# dp[i][j] 表示word1的前i个字符转换成word2前j个字符需要的最少次数
# 求 dp[n][m]
# dp[i][j] = 
#            dp[i-1][j-1], if word1[i-1] == word2[j-1]
#            min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1, else
# init: dp[0][:], dp[:][0]

class Solution:
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n+1)]
        for j in range(1, m+1):
            dp[0][j] = j
        for i in range(1, n+1):
            dp[i][0] = i
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        
        return dp[n][m]
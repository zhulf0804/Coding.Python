'''
题目思路不难: 状态转移方程容易写

难点1: 初始化条件, dp[0][j] 有多种p字符串可能匹配空串
难点2: 转移方差, 当p[j] == '*' and (s[i] == p[j-1] or p[j-1] == '.')时
            dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j-1] // or 后面的容易忽略

易错点: p 是空串则只能匹配空串
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[0] * (m + 1) for _ in range(n+1)]
        dp[0][0] = 1
        for j in range(1, m+1):
            if j == 2 and p[j-1] == '*':
                dp[0][j] = 1
            elif j > 2:
                if p[j-1] == '*' and dp[0][j-2] == 1:
                    dp[0][j] = 1
        if m == 0:
            return bool(dp[n][0])
        for i in range(1, n + 1):
            if i == 1 and (p[0] == '.' or p[0] == s[i-1]):
                dp[i][1] = 1
        for i in range(1, n+1):
            for j in range(2, m+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]
        return bool(dp[n][m])

s = "aaa"
p = "a*a"
a = Solution()
print(a.isMatch(s, p))

'''
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'
'''
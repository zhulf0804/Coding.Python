# class Solution:
#     def isMatch(self, s, p):
#         if len(s) == 0:
#             if len(p) == 0:
#                 return True
#             elif len(p) >= 2 and p[1] == '*':
#                 return self.isMatch(s, p[2:])
#             else:
#                 return False

#         if len(p) == 0:
#             return False
        
#         if len(p) == 1:
#             if p[0] == s[0] or p[0] == '.':
#                 return self.isMatch(s[1:], p[1:])
#             else:
#                 return False
#         else:
#             if p[1] == '*':
#                 if p[0] == s[0] or p[0] == '.':
#                     return self.isMatch(s[1:], p) or self.isMatch(s, p[2:]) or self.isMatch(s[1:], p[2:])
#                 else:
#                     return self.isMatch(s, p[2:])
#             else:
#                 if p[0] == s[0] or p[0] == '.':
#                     return self.isMatch(s[1:], p[1:])
#                 else:
#                     return False


class Solution:
    def isMatch(self, s, p):
        n, m = len(s), len(p)
        dp = [[0] * (m+1) for _ in range(n+1)]
        # dp[n][m]

        dp[0][0] = 1
        for i in range(2, m+1):
            if p[i-1] == '*' and dp[0][i-2]:
                dp[0][i] = 1
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
        
        return bool(dp[n][m])
        
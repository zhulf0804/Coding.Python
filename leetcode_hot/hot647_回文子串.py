# dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

# class Solution:
#     def countSubstrings(self, s):
#         n = len(s)
#         dp = [[0] * n for _ in range(n)]
#         ans = 0
#         for i in range(n):
#             dp[i][i] = 1
#             ans += dp[i][i]
#         for i in range(n-1):
#             if s[i] == s[i+1]:
#                 dp[i][i+1] = 1
#             ans += dp[i][i+1]

#         for l in range(3, n+1):
#             for i in range(n):
#                 if i + l - 1 < n:
#                     dp[i][i+l-1] = dp[i+1][i+l-2] and s[i] == s[i+l-1]
#                     ans += dp[i][i+l-1]
#         return ans

class Solution:
    def countSubstrings(self, s):
        n = len(s)
        ans = 0
        for i in range(n):
            k = 0
            while i - k >= 0 and i + k < n:
                if s[i-k] == s[i+k]:
                    ans += 1
                    k += 1
                else:
                    break

        for i in range(n-1):
            j = i + 1
            k = 0
            while i - k >= 0 and j + k < n:
                if s[i-k] == s[j+k]:
                    ans += 1
                    k += 1
                else:
                    break
        return ans
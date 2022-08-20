# class Solution:
#     def longestValidParentheses(self, s):
#         n = len(s)
#         stack = []
#         ids = []
#         i = 0
#         while i < n:
#             if s[i] ==')':
#                 if len(stack) > 0 and stack[-1][1] == '(':
#                     t = stack.pop()
#                     ids.append(i)
#                     ids.append(t[0])
#                 else:
#                     stack.append([i, s[i]])
#             else:
#                 stack.append([i, s[i]])
#             i += 1
#         ids = sorted(ids)
#         ans = 0
#         summ = 1
#         for i in range(1, len(ids)):
#             if ids[i] == ids[i-1] + 1:
#                 summ += 1
#             else:
#                 ans = max(ans, summ)
#                 summ = 1
#         if summ > 1:
#             ans = max(ans, summ)
#         return ans


# dp[i] = dp[i-2] + 2, s[i] == ')' and s[i-1] == '('
# dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2], s[i - dp[i-1] - 1] == '(' and s[i] == ')' and s[i-1] == ')'
# max(dp)
class Solution:
    def longestValidParentheses(self, s):  
        ans = 0 
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] += 2
                    if i - 2 >= 0:
                        dp[i] += dp[i-2]
                else:
                    if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                        dp[i] = dp[i-1] + 2
                        if i - dp[i-1] - 2 >= 0:
                            dp[i] += dp[i - dp[i-1] - 2]
            ans = max(ans, dp[i])
        return ans


a = '()()(()()()'
b = '(((()))'

s = Solution()
print(s.longestValidParentheses(b))
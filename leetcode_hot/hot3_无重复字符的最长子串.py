# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         if len(s) == 0:
#             return 0
#         dp = [1] * len(s)
#         pre = {s[0]:0}
#         for i in range(1, len(s)):
#             if s[i] in pre:
#                 pre_j = pre[s[i]]
#                 last_j = i - dp[i-1]
#                 if pre_j < last_j:
#                     dp[i] = dp[i-1] + 1
#                 else:
#                     dp[i] = i - pre_j
#             else:
#                 dp[i] = dp[i-1] + 1
#             pre[s[i]] = i
#         return max(dp)

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         if len(s) == 0:
#             return 0
#         dp = [1] * len(s)
#         pre = {s[0]:0}
#         for i in range(1, len(s)):
#             pre_j = pre.get(s[i], -2) + 1
#             last_j = i - dp[i-1]
#             dp[i] = i - max(pre_j, last_j) + 1
#             pre[s[i]] = i
#         return max(dp)

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         if len(s) == 0:
#             return 0
#         i, j = 0, 0
#         dict = {}
#         ans = 0
#         while j < len(s):
#             if s[j] in dict:
#                 i = max(dict[s[j]] + 1, i)    
#             ans = max(ans, j - i + 1)
#             dict[s[j]] = j
#             j += 1
#         return ans


class Solution:
    def lengthOfLongestSubstring(self, s):
        left, right = 0, 0
        window = {}
        ans = 0
        while right < len(s):
            c = s[right]
            if c in window:
                left = max(window[c] + 1, left)
            ans = max(ans, right - left + 1)
            window[c] = right
            right += 1 
        return ans



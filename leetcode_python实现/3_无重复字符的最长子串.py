class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        res = 1
        for i in range(1, len(s)):
            if s[i] not in s[i-dp[i-1]:i]:
                dp[i] = dp[i-1] + 1
            else:
                pos = s[i-dp[i-1]:i][::-1].find(s[i])
                dp[i] = 1 + pos
            if dp[i] > res:
                res = dp[i]
        return res

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        ans, dp, d = 1, [1] * n, {}
        d[s[0]] = 0
        for i in range(1, n):
            dp[i] = dp[i-1] + 1
            if s[i] in d:
                dp[i] = min(dp[i-1] + 1, i - d[s[i]])
            d[s[i]] = i
            ans = max(ans, dp[i])
        return ans
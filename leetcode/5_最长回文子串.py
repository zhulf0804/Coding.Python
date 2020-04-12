import numpy as np
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return s
        #dp = np.zeros((len(s), len(s)), dtype=np.int32)
        dp = [[0] * len(s) for _ in range(len(s))]
        max_length = 1
        loc = 0
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                max_length = 2
                loc = i
        for k in range(2, len(s)):
            for i in range(len(s) - k):
                if s[i] == s[i+k] and dp[i+1][i+k-1]:
                    dp[i][i+k] = 1
                    if k + 1 > max_length:
                        max_length = k + 1
                        loc = i

        return s[loc:loc+max_length]



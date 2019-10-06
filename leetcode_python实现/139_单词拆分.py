from typing import List
# 递归
class Solution_1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        for word in wordDict:
            if s.startswith(word):
                if self.wordBreak(s[len(word):], wordDict):
                    return True
        return False

# 记忆化搜索
class Solution_2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakCore(new_s, wordDict, memo):
            if not new_s:
                return True
            for word in wordDict:
                if new_s.startswith(word):
                    if new_s[len(word):] in memo:
                        flag = memo[new_s[len(word):]]
                    else:
                        flag = wordBreakCore(new_s[len(word):], wordDict, memo)
                        memo[new_s[len(word):]] = flag
                    if flag:
                        return True
            return False
        memo = {}
        return wordBreakCore(s, wordDict, memo)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = 1
                    break
        return dp[len(s)]


s = "leetcode"
wordDict = ["leet", "code"]
w = Solution()
w.wordBreak(s, wordDict)
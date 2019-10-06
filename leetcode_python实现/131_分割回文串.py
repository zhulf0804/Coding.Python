from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        l = len(s)
        dp = [[0] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = 1
            if i < l - 1 and s[i] == s[i+1]:
                dp[i][i+1] = 1
        for step in range(2, l):
            for i in range(l):
                if i + step >= l:
                    continue
                if s[i] == s[i+step] and dp[i+1][i+step-1]:
                    dp[i][i+step] = 1
        def parition_core(left, right, cur):
            if left > right:
                res.append(cur)
                return
            for i in range(left, right+1):
                if dp[left][i]:
                    parition_core(i+1, right, cur + [s[left:i+1]])
        parition_core(0, l - 1, [])
        return res

s = "aab"
ss = Solution()
print(ss.partition(s))


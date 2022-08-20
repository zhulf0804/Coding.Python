from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.res = []

        maxl, maxr = 0, 0
        for c in s:
            if c == '(':
                maxl += 1
            elif c == ')':
                maxr += 1
        self.mmax = min(maxl, maxr)

        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l != 0:
                    l -= 1
                else:
                    r += 1

        self.max_len = len(s) - l - r 

        def dfs(cur, i, s, l, r):
            if i == len(s):
                if l == r:
                    if len(cur) == self.max_len:
                        self.res.append(cur)
                return
            if l > self.mmax or r > self.mmax:
                return
            if r > l:
                return
            if s[i] == '(':
                dfs(cur+s[i], i+1, s, l+1, r)
                dfs(cur, i+1, s, l, r)
            elif s[i] == ')':
                dfs(cur+s[i], i+1, s, l, r+1)
                dfs(cur, i+1, s, l, r)
            else:
                dfs(cur+s[i], i+1, s, l, r)
            
        
        dfs('', 0, s, 0, 0)

        res_reduced = list(set(self.res))
        if len(res_reduced) == 0:
            return [""]
        return res_reduced

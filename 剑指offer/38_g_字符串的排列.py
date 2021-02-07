from typing import List

class Solution:
    def helper(self, cur, vst, s, res):
        if sum(vst) == len(vst):
            res.append(cur)
            return
        for i in range(len(s)):
            if not vst[i]:
                vst[i] = 1
                self.helper(cur + s[i], vst, s, res)
                vst[i] = 0
    def permutation(self, s: str) -> List[str]:
        n, res = len(s), []
        vst = [0] * n
        for i in range(n):
            vst[i] = 1
            self.helper(s[i], vst, s, res)
            vst[i] = 0
        return list(set(res))

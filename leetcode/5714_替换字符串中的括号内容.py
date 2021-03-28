from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}
        for k, v in knowledge:
            d[k] = v

        res = ''
        st, n = -1, len(s)
        left = False
        for i in range(n):
            if s[i] == '(':
                left = True
                st = i
            elif s[i] == ')':
                left = False
                res += d.get(s[st+1:i], '?')
            else:
                if not left:
                    res += s[i]
        return res

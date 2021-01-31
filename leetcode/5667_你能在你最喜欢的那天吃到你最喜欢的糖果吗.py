from typing import List

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        cur, summ = 0, []
        for v in candiesCount:
            cur += v
            summ.append(cur)
        for query in queries:
            t, d, k = query
            b = summ[t]
            a = 0 if t == 0 else summ[t-1]
            if k * (d + 1) > a and (d + 1) <= b:
                res.append(True)
            else:
                res.append(False)
        return res

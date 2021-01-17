from typing import List
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        d = {}
        mmax = 0
        for a, b in rectangles:
            mmin = min(a, b)
            mmax = max(mmin, mmax)
            d[mmin] = d.get(mmin, 0) + 1
        return d[mmax]

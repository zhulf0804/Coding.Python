from typing import List

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        mull, mulr = [1], [1]
        cur = 1
        for item in a:
            cur *= item
            mull.append(cur)
        cur = 1
        for item in reversed(a):
            cur *= item
            mulr.append(cur)
        mulr = list(reversed(mulr))

        res = []
        for i in range(len(a)):
            ans = mull[i] * mulr[i+1]
            res.append(ans)
        return res
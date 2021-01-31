from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        mmax = pow(10, n) - 1
        return list(range(1, mmax + 1))
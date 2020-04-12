from typing import List
from collections import Counter
# 超时
class Solution_1:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        res = 0
        D = list(sorted(D))
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    summ = A[i] + B[j] + C[k]
                    l, r = 0, len(D) - 1
                    while l <= r:
                        mid = (l + r) // 2
                        if summ + D[mid] > 0:
                            r = mid - 1
                        elif summ + D[mid] < 0:
                            l = mid + 1
                        else:
                            res += D.count(D[mid])
                            break
        return res


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dict = Counter([a + b for a in A for b in B])
        res = sum([dict.get(-c-d, 0) for c in C for d in D])
        return res




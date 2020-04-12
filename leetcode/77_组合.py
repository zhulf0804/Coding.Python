from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def combine_core(cur, left):
            if len(cur) == k:
                res.append(cur)
                return
            for i in range(len(left)):
                combine_core(cur + [left[i]], left[i+1:])
        combine_core([], [i for i in range(1, n+1)])
        #res = list(set([tuple(t) for t in res]))
        return res

n = 4
k = 2
s = Solution()
res = s.combine(n, k)
print(res)
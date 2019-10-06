from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def combinationSumCore(cur, new_target):
            if new_target == 0:
                res.append(sorted(cur))
                return
            if new_target < 0:
                return
            for candidate in candidates:
                combinationSumCore(cur + [candidate], new_target - candidate)
        combinationSumCore([], target)
        res = list(set([tuple(t) for t in res]))
        return res

candidates = [2,3,6,7]
target = 7
s = Solution()
res = s.combinationSum(candidates, target)
print(res)
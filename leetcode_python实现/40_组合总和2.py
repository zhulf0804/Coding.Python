from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def combinationSumCore(cur, new_target, new_candidates):
            if new_target == 0:
                res.append(sorted(cur))
                return
            #print(cur, new_target, new_candidates, "hello")
            if new_target < 0 or not new_candidates:
                return
            for i, candidate in enumerate(new_candidates):
                combinationSumCore(cur + [candidate], new_target - candidate, new_candidates[i+1:])
                #print(candidate, new_target, new_candidates[i+1:])
        combinationSumCore([], target, candidates)
        res = list(set([tuple(t) for t in res]))
        return res

candidates = [10,1,2,7,6,1,5]
target = 8
s = Solution()
res = s.combinationSum2(candidates, target)
print(res)
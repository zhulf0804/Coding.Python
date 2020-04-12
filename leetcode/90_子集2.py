from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def subset_core(cur, left):
            res.append(cur)
            if not left:
                return
            dic = {}
            for i in range(len(left)):
                if left[i] in dic:
                    continue
                else:
                    dic[left[i]] = 1
                    subset_core(cur + [left[i]], left[i + 1:])
        subset_core([], nums)
        res = list(set([tuple(t) for t in res]))
        return res

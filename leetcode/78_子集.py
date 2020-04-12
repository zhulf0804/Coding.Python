from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def subset_core(cur, left):
            res.append(cur)
            if not left:
                return
            for i in range(len(left)):
                subset_core(cur + [left[i]], left[i+1:])

        subset_core([], nums)
        return res

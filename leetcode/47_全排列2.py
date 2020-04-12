from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        #nums = sorted(nums)
        def permuteUniquceCore(cur, left):
            if not left:
                res.append(cur)
                return
            for i in range(len(left)):
                permuteUniquceCore(cur + [left[i]], left[:i] + left[i+1:])
        permuteUniquceCore([], nums)
        res = list(set(tuple(t) for t in res))
        return res

s = Solution()
res = s.permuteUnique([1, 1, 2])
print(res)
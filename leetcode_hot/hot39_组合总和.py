# class Solution:
#     def __init__(self):
#         self.mem_dict = {}

#     def combinationSum(self, candidates, target):
#         if target < 0:
#             return []
#         if target == 0:
#             return [[]]
#         if target in self.mem_dict:
#             return self.mem_dict[target]
#         cur_res = []
#         for candidate in candidates:
#             sub_res = self.combinationSum(candidates, target-candidate)
#             for item in sub_res:
#                 cur_res.append(list(sorted([candidate] + item)))
#         cur_res = [tuple(item) for item in cur_res]
#         res = list(set(cur_res))
#         res = [list(item) for item in res]
#         self.mem_dict[target] = res
#         return res

class Solution:

    def combinationSum(self, candidates, target):
        res = []

        def backtrack(candidates, target, begin, size, path):
            if target == 0:
                res.append(path)
                return
            if target < 0:
                return
            for i in range(begin, size):
                backtrack(candidates, target-candidates[i], i, size, path+[candidates[i]])
        
        backtrack(candidates, target, 0, len(candidates), [])
        return res
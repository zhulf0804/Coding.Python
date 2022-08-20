class Solution:
    def subsets(self, nums):
        res = []
        def backtrack(nums, begin, size, path):
            res.append(path)
            for i in range(begin, size):
                backtrack(nums, i+1, size, path + [nums[i]])
        backtrack(nums, 0, len(nums), [])
        return res
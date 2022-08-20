class Solution:
    def core(self, nums):
        n = len(nums)
        exist = False
        a, b = -1, -1
        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and nums[j] > nums[i]:
                j += 1
            if j == i + 1:
                continue
            exist = True
            a, b = i, j - 1
            return exist, a, b
        return exist, a, b

    def nextPermutation(self, nums):
        exist, a, b = self.core(nums)
        if exist:
            nums[a], nums[b] = nums[b], nums[a]
            nums[a+1:] = nums[a+1:][::-1]
        else:
            nums[:] = nums[::-1]
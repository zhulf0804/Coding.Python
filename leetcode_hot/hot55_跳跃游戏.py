class Solution:
    def canJump(self, nums):
        mmax = 0
        n = len(nums)
        for i in range(n):
            if i > mmax:
                return False
            mmax = max(i + nums[i], mmax)
        
        return True

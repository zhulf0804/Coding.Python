
from torch import mm


class Solution:
    def maxArea(self, height):
        mmax = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            mmax = max(mmax, area)
        return mmax


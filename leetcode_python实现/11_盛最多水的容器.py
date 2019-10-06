from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        starts = []
        ends = []
        max_height = -1
        for i in range(len(height)):
            if height[i] > max_height:
                starts.append([i, height[i]])
                max_height = height[i]

        max_height = -1
        for i in range(len(height)-1, -1, -1):
            if height[i] > max_height:
                ends.append([i, height[i]])
                max_height = height[i]

        mmax = 0
        for start in starts:
            for end in ends:
                area = (end[0] - start[0]) * min(end[1], start[1])
                if area > mmax:
                    mmax = area
        return mmax

height = [1,8,6,2,5,4,8,3,7]
s = Solution()
mmax = s.maxArea(height)
print(mmax)
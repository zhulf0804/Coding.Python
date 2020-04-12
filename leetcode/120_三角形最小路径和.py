from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        mmax = max(max(triangle))
        for i in range(1, h):
            for j in range(len(triangle[i])):
                mmin = max(triangle[i-1])
                if j < len(triangle[i-1]):
                    mmin = min(triangle[i-1][j], mmin)
                if j - 1 >= 0:
                    mmin = min(triangle[i-1][j-1], mmin)
                triangle[i][j] = mmin + triangle[i][j]
            #print(triangle)

        return sorted(triangle[-1])[0]

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

s = Solution()
res = s.minimumTotal(triangle)
print(res)
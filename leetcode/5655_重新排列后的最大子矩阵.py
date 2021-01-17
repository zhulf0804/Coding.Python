from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        up = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    up[i][j] = 1 if i == 0 else up[i-1][j] + 1
        ans = 0
        for i in range(n):
            vec = sorted(up[i])
            for j in range(m):
                cur = vec[j] * (m - j)
                ans = max(ans, cur)
        return ans

a = Solution()
matrix = [[1,0,1,0,1]]
print(a.largestSubmatrix(matrix))

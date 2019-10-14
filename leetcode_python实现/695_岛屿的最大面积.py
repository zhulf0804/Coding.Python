from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mmax_area = 0
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        def helper(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0
            if visited[x][y]:
                return 0
            visited[x][y] = 1
            if grid[x][y] == 0:
                return 0
            return 1 + helper(x - 1, y) + helper(x + 1, y) + helper(x, y - 1) + helper(x, y + 1)
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    area = helper(i, j)
                    if area > mmax_area:
                        mmax_area = area
        return mmax_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

obj = Solution()
print(obj.maxAreaOfIsland(grid))


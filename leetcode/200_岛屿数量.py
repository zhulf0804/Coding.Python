from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for i in range(m)]
        res = 0
        def search(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if not visited[x][y] and grid[x][y] == "1":
                visited[x][y] = 1
                search(x-1, y)
                search(x+1, y)
                search(x, y-1)
                search(x, y+1)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    search(i, j)
                    res += 1
        return res

grid = []

s = Solution()
print(s.numIslands(grid))
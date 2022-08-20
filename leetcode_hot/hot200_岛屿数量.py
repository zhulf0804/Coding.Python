class Solution:

    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        vst = [[0] * m for _ in range(n)]
        ans = 0

        def dfs(i, j, n, m):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if vst[i][j] or grid[i][j] == '0':
                return
            
            vst[i][j] = 1
            dfs(i-1, j, n, m)
            dfs(i+1, j, n, m)
            dfs(i, j-1, n, m)
            dfs(i, j+1, n, m)


        for i in range(n):
            for j in range(m):
                if not vst[i][j] and grid[i][j] == '1':
                    dfs(i, j, n, m)
                    ans += 1
        return ans

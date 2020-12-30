from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []
        for j in range(n):
            cols, col, flag = [], j, False
            for i in range(m):
                cols.append(col)
                cur = grid[i][col]
                col += grid[i][col]
                if col < 0 or col >= n:
                    res.append(-1)
                    flag = True
                    break
                adj = grid[i][col]
                if cur != adj:
                    res.append(-1)
                    flag = True
                    break
            if not flag:
                res.append(col)
        return res

a = Solution()
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
print(a.findBall(grid))
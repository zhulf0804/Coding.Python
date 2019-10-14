from typing import List
class Solution_1:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        res = [[0] * n for _ in range(m)]
        def helper(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return m + n + 2
            if visited[x][y]:
                return m + n + 2
            visited[x][y] = 1
            if matrix[x][y] == 0:
                visited[x][y] = 0
                return 0
            min_dist = min([helper(x+1, y), helper(x-1, y), helper(x, y+1), helper(x, y-1)]) + 1
            visited[x][y] = 0
            return min_dist

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    res[i][j] = helper(i, j)
        return res

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        res = [[0] * n for _ in range(m)]
        def helper(sx, sy, ex, ey, min_dist):
            if ex < 0 or ex >= m or ey < 0 or ey >= n:
                return m + n + 2
            if abs(ex - sx) + abs(ey - sy) >= min_dist:
                return min_dist

            if visited[ex][ey]:
                return m + n + 2
            if matrix[ex][ey] == 0:
                return 0

            visited[ex][ey] = 1
            min_dist = helper(sx, sy, ex+1, ey, float('inf')) + 1
            min_dist = min(helper(sx, sy, ex-1, ey, min_dist) + 1, min_dist)
            min_dist = min(helper(sx, sy, ex, ey+1, min_dist) + 1, min_dist)
            min_dist = min(helper(sx, sy, ex, ey-1, min_dist) + 1, min_dist)
            visited[ex][ey] = 0
            return min_dist

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    res[i][j] = helper(i, j, i, j, float('inf'))
            print(res[i])
        return res

matrix = [[1,0,1,1,0,0,1,0,0,1],
          [0,1,1,0,1,0,1,0,1,1],
          [0,0,1,0,1,0,0,1,0,0],
          [1,0,1,0,1,1,1,1,1,1],
          [0,1,0,1,1,0,0,0,0,1],
          [0,0,1,0,1,1,1,0,1,0],
          [0,1,0,1,0,1,0,0,1,1],
          [1,0,0,0,1,1,1,1,0,1],
          [1,1,1,1,1,1,1,0,1,0],
          [1,1,1,1,0,1,0,0,1,1]]

obj = Solution()
print(obj.updateMatrix(matrix))
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        res = 0
        def longestIncreasingPath(start, visited):
            x, y = start
            if longest[x][y] != 0:
                return longest[x][y]
            res = 1
            if x - 1 >= 0 and not visited[x-1][y] and matrix[x][y] < matrix[x-1][y]:
                visited[x-1][y] = 1
                res = max(res, 1 + longestIncreasingPath((x-1, y), visited))
                visited[x - 1][y] = 0
            if x + 1 < m and not visited[x+1][y] and matrix[x][y] < matrix[x+1][y]:
                visited[x + 1][y] = 0
                res = max(res, 1 + longestIncreasingPath((x+1, y), visited))
                visited[x + 1][y] = 0
            if y - 1 >= 0 and not visited[x][y-1] and matrix[x][y] < matrix[x][y-1]:
                visited[x][y - 1] = 1
                res = max(res, 1 + longestIncreasingPath((x, y-1), visited))
                visited[x][y - 1] = 0
            if  y + 1 < n and not visited[x][y+1] and matrix[x][y] < matrix[x][y + 1]:
                visited[x][y + 1] = 1
                res = max(res, 1 + longestIncreasingPath((x, y+1), visited))
                visited[x][y + 1] = 0
            longest[x][y] = res
            return res


        m, n = len(matrix), len(matrix[0])
        visited = [[0] * n for _ in range(m)]
        longest = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if longest[i][j] == 0:
                    visited[i][j] = 1
                    dist = longestIncreasingPath((i, j), visited)
                    visited[i][j] = 0
                    longest[i][j] = dist
                else:
                    dist = longest[i][j]
                if dist > res:
                    res = dist
        return res

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
s = Solution()
print(s.longestIncreasingPath(nums))
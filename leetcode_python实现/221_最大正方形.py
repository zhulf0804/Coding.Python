from typing import List
import numpy as np
class Solution_1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
        matrix = np.array(matrix, dtype=np.int)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    cur = 1
                    x, y = i, j
                    while x + 1 < m and y + 1 < n and matrix[x+1, y+1] == 1:
                        if np.sum(matrix[i:x+2, j: y+2]) == matrix[i:x+2, j:y+2].size:
                            cur = matrix[i:x+2, j: y+2].size
                            x += 1
                            y += 1
                        else:
                            break
                    if cur > res:
                        res = cur
        return res

class Solution_2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_len = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min([dp[i-1][j], dp[i-1][j-1], dp[i][j-1]]) + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
        return max_len ** 2

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_len = 0
        m, n = len(matrix), len(matrix[0])
        dp = [0]*(n+1)
        for i in range(1, m+1):
            tmp = 0
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    cur = min([dp[j-1], dp[j], tmp]) + 1
                    dp[j-1] = tmp
                    tmp = cur
                    #print(i, j, cur)
                    if cur > max_len:
                        max_len = cur
                else:
                    dp[j-1] = tmp
                    tmp = 0
            dp[n] = tmp
        return max_len ** 2


'''
matrix = [['1', '0', '1', '0', '0'],
          ['1', '0', '1', '1', '1'],
          ['1', '1', '1', '1', '1'],
          ['1', '0', '0', '1', '0']]
'''
matrix = [['1', '0', '1', '0'],
          ['1', '0', '1', '1'],
          ['1', '0', '1', '1'],
          ['1', '1', '1', '1']]

obj = Solution()
print(obj.maximalSquare(matrix))


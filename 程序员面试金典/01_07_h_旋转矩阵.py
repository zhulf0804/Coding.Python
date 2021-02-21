from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(i+1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for j in range(m // 2):
            for i in range(n):
                matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]
from typing import List

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n, m = len(matrix), len(matrix[0])
#         rows, cols = [], []
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     rows.append(i)
#                     cols.append(j)
#         for j in range(m):
#             for i in rows:
#                 matrix[i][j] = 0
#         for i in range(n):
#             for j in cols:
#                 matrix[i][j] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row, first_col = False, False
        n, m = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[0][i] == 0:
                first_row = True
                break
        for j in range(n):
            if matrix[j][0] == 0:
                first_col = True
                break

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0

        if first_row:
            for i in range(m):
                matrix[0][i] = 0
        if first_col:
            for i in range(n):
                matrix[i][0] = 0

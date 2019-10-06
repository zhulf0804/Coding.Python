from typing import List
class Solution_0:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        tag = 0.5
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    for i in range(rows):
                        if matrix[i][col] != 0:
                            matrix[i][col] = tag
                    for j in range(cols):
                        if matrix[row][j] != 0:
                            matrix[row][j] = tag

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != int(matrix[row][col]):
                    matrix[row][col] = 0
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row = False
        first_col = False

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row = True
                    if col == 0:
                        first_col = True
                    if row * col > 0:
                        matrix[0][col] = 0
                        matrix[row][0] = 0

        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(cols):
                    matrix[row][col] = 0

        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(rows):
                    matrix[row][col] = 0

        if first_row:
            for col in range(cols):
                matrix[0][col] = 0
        if first_col:
            for row in range(rows):
                matrix[row][0] = 0



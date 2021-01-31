from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        row, col = 0, m - 1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
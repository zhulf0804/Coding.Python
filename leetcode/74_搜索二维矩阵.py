from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        l = 0
        h = len(matrix) - 1
        while l < h - 1:
            mid = (l + h) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                h = mid - 1
            else:
                l = mid
        target_row = 0
        if matrix[h][0] > target:
            target_row = l
        else:
            target_row = h
        l = 0
        r = len(matrix[target_row]) - 1
        while l < r:
            mid = (l + r) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if matrix[target_row][l] == target:
            return True
        else:
            return False

matrix = [[1]]
target = 2
s = Solution()
s.searchMatrix(matrix, target)
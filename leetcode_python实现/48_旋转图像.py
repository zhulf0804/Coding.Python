from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                #print(i, j)
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                #print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][len(matrix) - 1 - j] =  matrix[i][len(matrix) - 1 - j], matrix[i][j]
        #print(matrix)

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s = Solution()
s.rotate(matrix)
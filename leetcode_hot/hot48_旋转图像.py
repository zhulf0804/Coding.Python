class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n // 2):
            for j in range(n):
                matrix[j][i], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[j][i]
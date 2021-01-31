from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return res
        n, m = len(matrix), len(matrix[0])
        for k in range((min(m, n) + 1) // 2):
            for j in range(k, m-k):
                res.append(matrix[k][j])
            for i in range(k+1, n-k):
                res.append(matrix[i][m-k-1])
            if n - k - 1 > k:
                for j in range(m-k-2, k-1, -1):
                    res.append(matrix[n-k-1][j])
            if m - k - 1 > k:
                for i in range(n-k-2, k, -1):
                    res.append(matrix[i][k])
        return res

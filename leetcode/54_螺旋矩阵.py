from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        steps = (min(m, n) + 1) // 2
        for step in range(steps):
            l, r, t, b = step, n - 1 - step, step, m - 1 - step
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            for i in range(t+1, b+1):
                res.append(matrix[i][r])
            if b != t:
                for i in range(r - 1, l - 1, -1):
                    res.append(matrix[b][i])
            if l != r:
                for i in range(b-1, t, -1):
                    res.append(matrix[i][l])
        return res
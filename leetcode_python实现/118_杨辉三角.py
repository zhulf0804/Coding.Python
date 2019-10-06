from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = []
        res.append([1])
        for i in range(1, numRows):
            lines = [1] * (i + 1)
            for j in range(1, i):
                lines[j] = res[i-1][j] + res[i-1][j - 1]
            res.append(lines)
        return res
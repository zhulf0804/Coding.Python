from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        rounds = (n + 1) // 2
        val = 1
        for round in range(rounds):
            l, r, t, b = round, n - 1 - round, round, n - 1 - round
            for i in range(l, r + 1):
                res[round][i] = val
                val += 1
            for i in range(t+1, b+1):
                res[i][r] = val
                val += 1
            if t != b:
                for i in range(r - 1, l - 1, -1):
                    res[b][i] = val
                    val += 1
            if l != r:
                for i in range(b - 1, t, -1):
                    res[i][l] = val
                    val += 1
        return res
from typing import List

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = matrix[0][0]
        res = [dp[0][0]]
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] ^ matrix[0][j]
            res.append(dp[0][j])
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] ^ matrix[i][0]
            res.append(dp[i][0])
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] ^ dp[i][j-1] ^ dp[i-1][j-1] ^ matrix[i][j]
                res.append(dp[i][j])
        res = sorted(res, reverse=True)
        return res[k-1]

from typing import List

# 优化的暴力
class Solution_1:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i][j-1] + 1 if j else 1
                    width = dp[i][j]
                    for k in range(i, -1, -1):
                        width = min(width, dp[k][j])
                        area = width * (i - k + 1)
                        if area >= max_area:
                            max_area = area
        return max_area

# 柱状图递增栈的思想
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        dp = [[0] * n for _ in range(m)]
        stack = [[-1] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i][j-1] + 1 if j else 1
                width = dp[i][j]
                while len(stack[j]) > 1 and width < dp[stack[j][-1]][j]:
                    top = stack[j].pop()
                    area = dp[top][j] * (i - stack[j][-1] - 1)
                    max_area = max(area, max_area)
                stack[j].append(i)
        for i in range(n):
            while len(stack[i]) > 1:
                top = stack[i].pop()
                area = dp[top][i] * (m - stack[i][-1] - 1)
                max_area = max(area, max_area)
        return max_area

matrix = [["0","1"],["1","0"]]
obj = Solution()
print(obj.maximalRectangle(matrix))
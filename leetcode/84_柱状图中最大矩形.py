from typing import List

# 超出内存限制
class Solution_1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        dp = [[float('inf')] * n  for _ in range(n)]
        max_area = 0
        for i in range(n):
            dp[i][i] = heights[i]
            max_area = max(max_area, heights[i])
        for i in range(n):
            for j in range(i+1, n):
                dp[i][j] = min(dp[i][j-1], heights[j])
                area = dp[i][j] * (j - i + 1)
                max_area = max(area, max_area)
        return max_area

# 将二维降成一维, 超出时间限制, 但通过了94个测试用例（一共96个）
class Solution_2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        dp = [float('inf')] * n
        max_area = 0
        for i in range(n):
            dp[i] = heights[i]
            max_area = max(max_area, dp[i])
            for j in range(i+1, n):
                dp[j] = min(dp[j-1], heights[j])
                area = dp[j] * (j - i + 1)
                max_area = max(area, max_area)
        return max_area

# 递增栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        stack.append(-1)
        max_area = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                area = heights[top] * (i - stack[-1] - 1)
                max_area = max(max_area, area)
            stack.append(i)
        while len(stack) > 1:
            top = stack.pop()
            max_area = max(max_area, heights[top] * (len(heights) - stack[-1] - 1))
        return max_area




heights = [2,1,5,6,2,3]
obj = Solution()
print(obj.largestRectangleArea(heights))
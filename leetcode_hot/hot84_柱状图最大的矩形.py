class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = []
        max_area = 0
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                l = stack[-1] if len(stack) > 0 else -1
                area = heights[j] * (i - l - 1)
                max_area = max(max_area, area)
            stack.append(i)
        for i in range(len(stack)):
            l = -1 if i == 0 else stack[i-1]
            area = heights[stack[i]] * (n - 1 - l)
            max_area = max(area, max_area)
        return max_area
                
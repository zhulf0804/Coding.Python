class Solution:
    def maximalRectangle(self, matrix):
        n, m = len(matrix), len(matrix[0])
        max_area = 0
        heights = [0] * m

        def core(heights):
            n = len(heights)
            max_area = 0
            stack = []
            for i in range(n):
                while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                    j = stack.pop()
                    l = stack[-1] if len(stack) > 0 else -1
                    area = heights[j] * (i - l - 1)
                    max_area = max(max_area, area)
                stack.append(i)
            
            for i in range(len(stack)):
                l = -1 if i == 0 else stack[i-1]
                area = heights[stack[i]] * (n - 1 - l)
                max_area = max(max_area, area)
            return max_area

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += int(matrix[i][j]) 
            area = core(heights)
            max_area = max(area, max_area)
        return max_area
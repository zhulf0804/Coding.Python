# class Solution:
#     def trap(self, height):
        
#         def helper(height):
#             stack = []
#             n = len(height)
#             for i in range(n):
#                 if len(stack) == 0 or height[i] >= height[stack[-1]]:
#                     stack.append(i)
            
#             res = 0
#             for j in range(1, len(stack)):
#                 s = stack[j-1]
#                 e = stack[j]
#                 ans = 0
#                 for k in range(s+1, e):
#                     ans += (height[s] - height[k])
#                 res += ans
#             return res, stack[-1]

#         res1, i = helper(height)
#         res2, _ = helper(height[i:][::-1])
#         return res1 + res2

# class Solution:
#     def trap(self, height):
        
#         def helper(height):
#             stack = []
#             n = len(height)
#             res, ans = 0, 0
#             for i in range(n):
#                 if len(stack) == 0 or height[i] >= height[stack[-1]]:
#                     stack.append(i)
#                     res += ans
#                     ans = 0
#                 else:
#                     ans += (height[stack[-1]] - height[i])
#             return res, stack[-1]

#         res1, i = helper(height)
#         res2, _ = helper(height[i:][::-1])
#         return res1 + res2

# class Solution:
#     def trap(self, height):
#         n = len(height)
#         left, right = 1, n - 2
#         max_left, max_right = 0, 0
#         ans = 0
#         while left <= right:
#             if height[left-1] < height[right+1]:
#                 max_left = max(max_left, height[left-1])
#                 if height[left] < max_left:
#                     ans += (max_left - height[left])
#                 left += 1
#             else:
#                 max_right = max(max_right, height[right+1])
#                 if height[right] < max_right:
#                     ans += (max_right - height[right])
#                 right -= 1
#         return ans

class Solution:
    def trap(self, height):
        n = len(height)
        stack = []
        ans = 0
        for i in range(n):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                j = stack.pop()
                if len(stack) == 0:
                    break
                h = min(height[stack[-1]], height[i]) - height[j]
                l = i - stack[-1] - 1
                ans += (l * h) 
            stack.append(i)
        return ans

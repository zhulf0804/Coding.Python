class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        d = {temperatures[-1]:n-1}
        res = [0] * n
        for i in range(n-2, -1, -1):
            t = temperatures[i]
            near = n + 1
            for j in range(t+1, 101):
                if j in d:
                    near = min(near, d[j])
            if near == n + 1:
                res[i] = 0
            else:
                res[i] = near-i
            d[t] = i
        
        return res

# class Solution:
#     def dailyTemperatures(self, temperatures):
#         n = len(temperatures)
        
#         stack = []    
#         res = [0] * n
#         for i in range(n-1, -1, -1):
#             while len(stack) > 0 and temperatures[i] >= temperatures[stack[-1]]:
#                 stack.pop()
#             if len(stack) == 0:
#                 ans = 0
#             else:
#                 ans = stack[-1] - i
#             res[i] = ans
#             stack.append(i)
#         return res

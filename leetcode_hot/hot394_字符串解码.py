# class Solution:
#     def decodeString(self, s):
#         n = len(s)
#         stack, i = [], 0
#         while i < n:
#             if s[i] == ']':
#                 tmp_s = ''
#                 t = stack.pop()
#                 while t != '[':
#                     tmp_s = t + tmp_s
#                     t = stack.pop()
#                 tmp_n, mul = 0, 1
#                 t = stack.pop()
#                 while t >= '0' and t <= '9':
#                     tmp_n = tmp_n + int(t) * mul
#                     mul *= 10
#                     if stack:
#                         t = stack.pop()
#                     else:
#                         break
#                 if stack:
#                     stack.append(t)
#                 tmp_s = tmp_s * tmp_n
#                 for w in tmp_s:
#                     stack.append(w)
#             else:
#                 stack.append(s[i])
#             i += 1
#         return ''.join(stack)        
                       
class Solution:
    def decodeString(self, s):
        res, multi, stack = '', 0, []
        for w in s:
            if w == '[':
                stack.append([multi, res])
                multi, res = 0, ''
            elif w == ']':
                last_multi, last_res = stack.pop()
                res = last_res + last_multi * res
            elif w >= '0' and w <= '9':
                multi = multi * 10 + int(w)
            else:
                res += w
        return res
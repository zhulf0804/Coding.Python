# class Solution:
#     def reconstructQueue(self, people):
#         n = len(people)
#         people = sorted(people, key=lambda x:x[0])
#         res = [0] * n
#         vst = [0] * n
#         for item in people:
#             a, b = item
#             i, j = 0, 0
#             while j < n:
#                 if not vst[j] or res[j][0] >= a:
#                     i += 1
#                     if i == b + 1:
#                         vst[j] = 1
#                         break
#                 j += 1
#             res[j] = item
#         return res
            
class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        res = []
        for p in people:
            p0, p1 = p
            if len(res) <= p1:
                res.append(p)
            else:
                res.insert(p1, p)
        return res
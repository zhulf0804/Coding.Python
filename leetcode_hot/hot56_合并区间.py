# class Solution:
#     def merge(self, intervals):
#         intervals = list(sorted(intervals, key=lambda x:x[0]))
#         n = len(intervals)
#         res = []
#         cur, i = intervals[0], 1
#         while i < n:
#             x2, y2 = intervals[i]
#             if x2 <= cur[1]:
#                 cur[1] = max(cur[1], y2)
#             else:
#                 res.append(cur)
#                 cur = intervals[i]
#             i += 1
#         res.append(cur)
#         return res

class Solution:
    def merge(self, intervals):
        intervals = list(sorted(intervals, key=lambda x:x[0]))
        n = len(intervals)
        res = []
        j, i = 0, 1
        x, y = intervals[j]
        while i < n:
            x2, y2 = intervals[i]
            if x2 <= y:
                y = max(y, y2)
            else:
                res.append([x, y])
                j = i
                x, y = intervals[j]
            i += 1
        res.append([x, y])
        return res


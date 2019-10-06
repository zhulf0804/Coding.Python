from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=(lambda x:x[0]))
        res = []
        length = len(intervals)
        i = 0
        while i < length:
            j = i + 1
            while j < length and intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                j += 1
            res.append(intervals[i])
            i = j
        return res

intervals = [[1, 4], [0, 4]]

s = Solution()
res = s.merge(intervals)
print(res)
from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = []
        for b, a in classes:
            add = (a - b) / (a * (a + 1))
            heapq.heappush(q, (-add, b, a))
        while extraStudents > 0:
            addm, b, a = heapq.heappop(q)
            a += 1
            b += 1
            add = (a - b) / (a * (a + 1))
            heapq.heappush(q, (-add, b, a))
            extraStudents -= 1
        pass_rate = 0
        while q:
            addm, b, a = heapq.heappop(q)
            pass_rate += (b / a)
        return pass_rate / len(classes)

a = Solution()
classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
print(a.maxAverageRatio(classes, extraStudents))
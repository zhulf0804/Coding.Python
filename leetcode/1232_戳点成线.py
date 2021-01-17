from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        xs = [item[0] for item in coordinates]
        if len(set(xs)) == 1:
            return True
        if len(set(xs)) < n:
            return False
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for i in range(2, n):
            x3, y3 = coordinates[i]
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False
        return True

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
a = Solution()
print(a.checkStraightLine(coordinates))
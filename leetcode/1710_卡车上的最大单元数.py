from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True)
        ans, cur = 0, 0
        for x, y in boxTypes:
            if cur + x <= truckSize:
                cur += x
                ans += y * x
            else:
                l = truckSize - cur
                ans += y * l
                break
        return ans


a = Solution()
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(a.maximumUnits(boxTypes, truckSize))
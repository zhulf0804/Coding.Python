from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        pre = [1, 1]
        for i in range(2, rowIndex+1):
            cur = [1] * (i + 1)
            for j in range(1, i):
                cur[j] = pre[j] + pre[j - 1]
            pre = cur

        return cur

rowIndex = 3

s = Solution()
print(s.getRow(3))
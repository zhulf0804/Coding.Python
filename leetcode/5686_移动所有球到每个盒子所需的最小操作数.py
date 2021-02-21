from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = []
        for i in range(n):
            ans = 0
            for j in range(n):
                if i != j:
                    if boxes[j] == '1':
                       ans += abs(j - i)
            res.append(ans)
        return res
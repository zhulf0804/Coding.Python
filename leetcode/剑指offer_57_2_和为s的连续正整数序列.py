from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        small, big = 1, 2
        curSum = small + big
        while small <= target // 2:
            if curSum == target:
                res.append(list(range(small, big + 1)))
                curSum -= small
                small += 1
            elif curSum > target:
                curSum -= small
                small += 1
                continue
            else:
                big += 1
                curSum += big
        return res
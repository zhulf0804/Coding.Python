from typing import List
from functools import cmp_to_key
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def cmp(x, y):
            if x[0] > y[0] or (x[0] == y[0] and x[1] < y[1]):
                return 1
            if x[0] == y[0] and x[1] == y[1]:
                return 0
            if x[0] < y[0] or (x[0] == y[0] and x[1] > y[1]):
                return -1
        people = sorted(people, key=cmp_to_key(lambda x, y: cmp(x, y)), reverse=True)
        res = []
        for item in people:
            res.insert(item[1], item)
        return res

obj = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
obj.reconstructQueue(people)
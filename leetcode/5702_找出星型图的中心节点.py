from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = []
        a.extend(edges[0])
        a.extend(edges[1])
        return sum(a) - sum(set(a))
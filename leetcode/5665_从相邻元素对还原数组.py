from typing import List
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs)
        d = defaultdict(list)
        vst = {}
        for a, b in adjacentPairs:
            d[a].append(b)
            d[b].append(a)
            vst[a] = False
            vst[b] = False
        st = -1
        for k, v in d.items():
            if len(v) == 1:
                st = k
                break
        i, res = 1, [st]
        vst[st] = True
        while i < n + 1:
            vs = d[st]
            for v in vs:
                if not vst[v]:
                    vst[v] = True
                    res.append(v)
                    st = v
            i += 1
        return res

a = Solution()
adjacentPairs = [[100000,-100000]]
print(a.restoreArray(adjacentPairs))
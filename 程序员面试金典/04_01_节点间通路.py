from typing import List

class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        if start == target:
            return True
        vst = [0] * n
        g = [[] for _ in range(n)]
        for a, b in graph:
            g[a].append(b)
        cur = start
        i, l = 0, [start]
        while i < len(l):
            cur = l[i]
            for item in g[cur]:
                if item == target:
                    return True
                if vst[item]:
                    continue
                vst[item] = 1
                l.append(item)
            i += 1
        return False

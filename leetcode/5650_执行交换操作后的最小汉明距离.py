from typing import List
from collections import defaultdict

def find(p, uf):
    if uf[p] < 0:
        return p
    uf[p] = find(uf[p], uf)
    return uf[p]

def union(p, q, uf):
    proot = find(p, uf)
    qroot = find(q, uf)
    if proot == qroot:
        return
    elif uf[proot] > uf[qroot]:
        uf[qroot] += uf[proot]
        uf[proot] = qroot
    else:
        uf[proot] += uf[qroot]
        uf[qroot] = proot

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = [-1 for _ in range(n)]
        for u, v in allowedSwaps:
            ufather, vfather = find(u, uf), find(v, uf)
            if ufather != vfather:
                union(u, v, uf)
        d = defaultdict(list)
        for i in range(n):
            par = find(i, uf)
            d[par].append(i)
        vst = [0] * n
        ans = 0
        for k, v in d.items():
            d1, d2 = {}, {}
            for idx in v:
                vst[idx] = 1
                d1[source[idx]] = d1.get(source[idx], 0) + 1
                d2[target[idx]] = d2.get(target[idx], 0) + 1
            for tk, tv in d2.items():
                ans += max(tv - d1.get(tk, 0), 0)
        for idx in range(n):
            if vst[idx] == 0:
                if source[idx] != target[idx]:
                    ans += 1
        return ans

a = Solution()
source = [1,2,3,4]
target = [2,1,4,5]
allowedSwaps = [[0,1],[2,3]]

print(a.minimumHammingDistance(source, target, allowedSwaps))

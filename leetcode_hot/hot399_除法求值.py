from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for equa, value in zip(equations, values):
            a, b = equa
            graph[a][b] = value
            graph[b][a] = 1.0 / value
        
        def dfs(s, e):
            if s not in graph or e not in graph:
                return -1
            if s == e:
                return 1
            for dict in graph[s].items():
                k, v = dict
                if k not in visited:
                    visited.add(k)
                    ans = dfs(k, e)
                    if ans != -1:
                        return ans * graph[s][k]
                        
            return -1

        res = []
        for query in queries:
            a, b = query
            visited = set()
            ans = dfs(a, b)
            res.append(ans)
        return res
from typing import List

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        d = [[0] * n for _ in range(n)]
        indegree = [0] * n
        for a, b in edges:
            d[a-1][b-1] = 1
            d[b-1][a-1] = 1
            indegree[a-1] += 1
            indegree[b-1] += 1
        ans = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                if d[i][j] == 1:
                    for k in range(j+1, n):
                         if d[i][k] == 1 and d[j][k] == 1:
                            ans = min(ans, indegree[i] + indegree[j] + indegree[k] - 6)
        if ans == float('inf'):
            return -1
        return ans


n = 6
edges = [[6,5],[4,3],[5,1],[1,4],[2,3],[4,5],[2,6],[1,3]]
a = Solution()
print(a.minTrioDegree(n, edges))
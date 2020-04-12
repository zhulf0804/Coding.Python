# https://leetcode-cn.com/problems/n-queens/

from typing import List

class Solution:
    res = []
    def check(self, cur, x):
        if x == 0 or x == 1:
            return True
        x0, y0 = x, cur[x-1]
        for i in range(0, x-1):
            x1, y1 = i + 1, cur[i]
            if abs(x0 - x1) == abs(y0 - y1):
                return False
        return True

    def dfs(self, n, x, visited, cur):
        if not self.check(cur, x-1):
            return
        if x == n + 1:
            tmp = []
            for i in range(n):
                tmp.append('.' * (cur[i] - 1) + 'Q' + '.' * (n - cur[i]))
            self.res.append(tmp)
            return
        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = 1
                self.dfs(n, x + 1, visited, cur + [i])
                visited[i] = 0
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        visited = [0] * (n + 1)
        self.dfs(n, 1, visited, [])
        return self.res

s = Solution()
print(s.solveNQueens(1))
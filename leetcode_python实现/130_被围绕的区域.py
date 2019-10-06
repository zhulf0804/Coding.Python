from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        boarder = [[0] * n for _ in range(m)]
        def dfs(x, y):
            if x - 1 >= 0 and board[x-1][y] == 'O' and not boarder[x-1][y]:
                boarder[x-1][y] = 1
                dfs(x-1, y)
            if x + 1 < m and board[x+1][y] == 'O' and not boarder[x+1][y]:
                boarder[x+1][y] = 1
                dfs(x+1, y)
            if y - 1 >= 0 and board[x][y-1] == 'O' and not boarder[x][y-1]:
                boarder[x][y-1] = 1
                dfs(x, y-1)
            if y + 1 < n and board[x][y+1] == 'O' and not boarder[x][y+1]:
                boarder[x][y+1] = 1
                dfs(x, y+1)
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == 'O' and not boarder[i][j]:
                    boarder[i][j] = 1
                    dfs(i, j)
        for j in [0, n-1]:
            for i in range(m):
                if board[i][j] == 'O' and not boarder[i][j]:
                    boarder[i][j] = 1
                    dfs(i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not boarder[i][j]:
                    board[i][j] = 'X'

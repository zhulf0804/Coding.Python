class Solution:
    def exist(self, board, word):
        n, m = len(board), len(board[0])
        t = len(word)

        def dfs(board, i, j, word, k, mask):
            if k == t:
                return True
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if mask[i][j]:
                return False
            if board[i][j] == word[k]:
                mask[i][j] = 1
                exist1 = dfs(board, i + 1, j, word, k+1, mask)
                exist2 = dfs(board, i - 1, j, word, k+1, mask)
                exist3 = dfs(board, i, j - 1, word, k+1, mask)
                exist4 = dfs(board, i, j + 1, word, k+1, mask)
                mask[i][j] = 0
                return exist1 or exist2 or exist3 or exist4
            return False

        for i in range(n):
            for j in range(m):
                mask = [[0] * m for _ in range(n)]
                ans = dfs(board, i, j, word, 0, mask)
                if ans:
                    return True
        return False

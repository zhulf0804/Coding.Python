from typing import List

class Solution:
    def exist_core(self, board, i, j, word, vst):
        n, m = len(board), len(board[0])
        if len(word) == 0:
            return True
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        if board[i][j] != word[0] or vst[i][j] == 1:
            return False
        vst[i][j] = 1
        res = self.exist_core(board, i-1, j, word[1:], vst) \
              or self.exist_core(board, i+1, j, word[1:], vst) \
              or self.exist_core(board, i, j-1, word[1:], vst) \
              or self.exist_core(board, i, j+1, word[1:], vst)
        vst[i][j] = 0
        return res
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        vst = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if self.exist_core(board, i, j, word, vst):
                    return True
        return False

board = [["b"],["a"],["b"]]
word = "bbabab"
a = Solution()
print(a.exist(board, word))
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        flag = [[0] * n for i in range(m)]

        def exist_core(new_world, i, j, flag):
            if not new_world:
                return True
            if i - 1 >= 0 and not flag[i-1][j] and board[i-1][j] == new_world[0]:
                flag[i-1][j] = 1
                t = exist_core(new_world[1:], i-1, j, flag)
                if t:
                    return True
                flag[i - 1][j] = 0
            if i + 1 < m and not flag[i+1][j] and board[i+1][j] == new_world[0]:
                flag[i+1][j] = 1
                b = exist_core(new_world[1:], i+1, j, flag)
                if b:
                    return True
                flag[i + 1][j] = 0
            if j - 1 >= 0 and not flag[i][j-1] and board[i][j-1] == new_world[0]:
                flag[i][j-1] = 1
                l = exist_core(new_world[1:], i, j-1, flag)
                if l:
                    return True
                flag[i][j-1] = 0
            if j + 1 < n and not flag[i][j+1] and board[i][j+1] == new_world[0]:
                flag[i][j+1] = 1
                r = exist_core(new_world[1:], i, j+1, flag)
                if r:
                    return True
                flag[i][j+1] = 0
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag[i][j] = 1
                    if exist_core(word[1:], i, j, flag):
                        return True
                    flag[i][j] = 0
        return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
s = Solution()
print(s.exist(board, word))
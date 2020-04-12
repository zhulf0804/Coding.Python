from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[int]]) -> bool:
        dict_row = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dict_col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dict_box = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == ".":
                    continue
                if num not in dict_row[i] and num not in dict_col[j] and num not in dict_box[3 * (i // 3) + (j // 3)]:
                    dict_row[i][num] = 1
                    dict_col[j][num] = 1
                    dict_box[3 * (i // 3) + (j // 3)][num] = 1
                else:
                    return False

        return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

s = Solution()
s.isValidSudoku(board)
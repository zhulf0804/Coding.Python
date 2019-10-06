from typing import List
import copy

# 辅助数组
class Solution_1:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = copy.deepcopy(board)
        m, n = len(board), len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n and board_copy[i + x][j + y] == 1:
                            count += 1
                if board_copy[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 0
                else:
                    if count == 3:
                        board[i][j] = 1

# 不适用辅助数组, 修改数组，不改变活/死的状态
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n and board[i + x][j + y] >= 1:
                            count += 1
                if board[i][j] == 1:
                    board[i][j] += count
                else:
                    board[i][j] -= count
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] >= 1:
                    if board[i][j] - 1 > 3 or board[i][j] - 1 < 2:
                        board[i][j] = 0
                    else:
                        board[i][j] = 1
                    continue
                if board[i][j] <= 0:
                    if board[i][j] == -3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0

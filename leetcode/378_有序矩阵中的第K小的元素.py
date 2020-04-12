from typing import List
class Solution_1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flatten = []
        for i in range(len(matrix)):
            flatten.extend(matrix[i])
        return sorted(flatten)[k-1]

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def helper(n):
            count = 0
            row = len(matrix) - 1
            col = 0
            while row >= 0 and col < len(matrix):
                if matrix[row][col] > n:
                    row -= 1
                else:
                    count += row + 1
                    col += 1
            return count
        low, high = matrix[0][0], matrix[len(matrix) - 1][len(matrix) - 1]
        while low < high:
            mid = (low + high) // 2
            if helper(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
s = Solution()
print(s.kthSmallest(matrix, k))
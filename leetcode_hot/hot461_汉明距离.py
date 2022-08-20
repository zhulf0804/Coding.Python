# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         z = x ^ y
#         ans = 0
#         while z:
#             ans += (z & 1)
#             z >>= 1
#         return ans

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        ans = 0
        while z:
            z &= (z - 1)
            ans += 1
        return ans
        
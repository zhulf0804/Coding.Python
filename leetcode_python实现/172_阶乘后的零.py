class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 0
        k = 5
        while k <= n:
            num += n//k
            k *= 5
        return num
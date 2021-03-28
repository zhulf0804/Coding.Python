class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return pow(3, a)
        elif b == 1:
            return pow(3, a-1) * 4
        else:
            return pow(3, a) * 2

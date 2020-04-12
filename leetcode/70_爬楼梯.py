class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        c = 3
        while c <= n:
            tmp = a + b
            a = b
            b = tmp
            c += 1
        return b


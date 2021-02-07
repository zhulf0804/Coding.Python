class Solution:
    def add(self, a: int, b: int) -> int:
        z = 0xffffffff
        a, b = a & z, b & z
        while b != 0:
            a, b = a ^ b, ((a & b) << 1) & z
        if a > 0x7fffffff:
            a = ~(a ^ z)
        return a

a, b = -2, 1
c = Solution()
print(c.add(a, b))
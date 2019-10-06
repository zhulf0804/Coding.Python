class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x & y
        b = x | y
        def get_bits(val):
            res = 0
            while val:
                res += val&1
                val = val >> 1
            return res
        return get_bits(b) - get_bits(a)
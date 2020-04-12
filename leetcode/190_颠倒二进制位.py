class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n).split('b')[1]
        val = 0
        for i in range(len(b)):
            bit = int(b[i])
            val += bit * 2 ** (i + 32 - len(b))
        return val

n = 43261596
obj = Solution()
print(obj.reverseBits(n))
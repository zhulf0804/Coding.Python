class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = (a & b) << 1
        cur = a ^ b
        ind = 1
        while carry:
            a, b = cur, carry
            carry = (a & b) << 1
            cur = a ^ b
        return cur

a, b = -1, 1
s = Solution()
s.getSum(a, b)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        for i in range(32):
            num += n & 1
            n = n >> 1
        return num
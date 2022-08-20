class Solution:
    def countBits(self, n):
        if n == 0:
            return [0]
        res = [0] * (n + 1)
        for i in range(1, n+1):
            if i % 2 == 1:
                res[i] = res[i-1] + 1
            else:
                res[i] = res[i//2]
        return res
            
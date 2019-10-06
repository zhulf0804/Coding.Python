class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while n != 1:
            if n in d:
                return False
            d[n] = 1
            summ = 0
            while n != 0:
                val = n % 10
                n = n // 10
                summ += val * val
            n = summ
        return True
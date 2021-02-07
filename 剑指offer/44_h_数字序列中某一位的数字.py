class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        summ, base, mul = 10, 90, 2
        while summ + base * mul < n:
            summ += base * mul
            base *= 10
            mul += 1
        n = n - summ
        v = str(n // mul + base // 9)
        n -= n // mul * mul
        return int(v[n])

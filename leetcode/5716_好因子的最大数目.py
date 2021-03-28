import math

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors <= 3:
            return primeFactors
        tmp = pow(10, 9) + 7
        a, b = primeFactors // 3, primeFactors % 3
        if b == 0:
            return pow(3, a, tmp)
        elif b == 1:
            return (pow(3, a - 1, tmp) * 4) % tmp
        else:
            return (pow(3, a, tmp) * 2) % tmp


primeFactors = 545918790
a = Solution()
print(a.maxNiceDivisors(primeFactors))

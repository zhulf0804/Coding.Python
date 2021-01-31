class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        flags = []
        tf = 1
        if n < 0:
            tf, n = -1, -n
        while n != 1:
            flags.append(n % 2)
            n = n // 2
        ans = x
        for flag in reversed(flags):
            ans = ans * ans
            if flag == 1:
                ans = ans * x
        if tf == -1:
            ans = 1 / ans
        return ans


'''
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
'''
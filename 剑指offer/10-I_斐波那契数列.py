class Solution:
    def fib(self, n: int) -> int:
        m = 1000000007
        a = [0, 1]
        if n <= 1:
            return a[n]
        for i in range(2, n+1):
            tmp = (a[0] + a[1]) % m
            a[0] = a[1]
            a[1] = tmp
        return a[1]

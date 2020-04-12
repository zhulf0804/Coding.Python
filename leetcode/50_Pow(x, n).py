class Solution:
    '''
    def myPow(self, x: float, n: int) -> float:
        flag1 = 1 if x >= 0 else (-1) ** (abs(n) % 2)
        flag2 = 1 if n >=0 else 0
        x = abs(x)
        n = abs(n)
        z = []
        while n > 1:
            z.append(n % 2)
            n = n // 2
        print(z)
        res = x
        for i in range(len(z) - 1, -1, -1):
            res = res ** 2
            if z[i] == 1:
                res = x * res
            print(res)
        if flag2 == 0:
            res = 1 / res
        res *= flag1
        return res
    '''

    def myPow(self, x: float, n: int) -> float:
        judge = True
        if n < 0:
            n = -n
            judge = False
        res = 1
        while n > 0:
            if n % 2 != 0:
                res *= x
            x *= x
            n = n // 2
        return res if judge else 1 / res


x = 2.00000
n = -2147483648
#n = 10
s = Solution()
res = s.myPow(x, n)
print(res)
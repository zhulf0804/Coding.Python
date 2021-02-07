'''
第一次不能ac
第二次，当 item * k > res[-1]时停止就无需继续判断，停止for循环即可，
时间复杂度应该是一样的，可能与大数的乘法有关吧。
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        res = [1]
        for i in range(2, n+1):
            pre = res[-1]
            mmin = float('inf')
            for k in [2, 3, 5]:
                for item in res:
                    if item * k > pre:
                        mmin = min(mmin, item * k)
                        break
            res.append(mmin)
        return res[-1]

'''
1 是丑数。
n 不超过1690。
10 -> 12
'''
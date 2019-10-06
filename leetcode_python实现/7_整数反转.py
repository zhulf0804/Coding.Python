# TBD
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        x_str = str(x)[::-1].lstrip('0')
        result = flag * int(x_str)
        if result > pow(2, 31) - 1 or result < -pow(2, 31):
            return 0
        return result


x = -1230


s = Solution()
result = s.reverse(x)
print(result)

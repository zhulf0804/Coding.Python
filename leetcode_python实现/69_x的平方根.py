class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid
        return left - 1


s = Solution()
res = s.mySqrt(4)
print(res)
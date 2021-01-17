class Solution:
    def countDigitOne(self, n: int) -> int:
        high, low, cur, digit = n // 10, 0, n % 10, 1
        ans = 0
        while high != 0 or cur != 0:
            if cur == 0:
                v = high * digit
            elif cur == 1:
                v = high * digit + low + 1
            else:
                v = high * digit + digit
            ans += v
            low += cur * digit
            cur = high % 10
            high = high // 10
            digit *= 10
        return ans

a = Solution()
print(a.countDigitOne(12))
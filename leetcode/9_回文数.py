class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        x_str = str(x)
        l = 0
        r = len(x_str) - 1
        while r > l:
            if x_str[l] == x_str[r]:
                l += 1
                r -= 1
                continue
            return False
        return True
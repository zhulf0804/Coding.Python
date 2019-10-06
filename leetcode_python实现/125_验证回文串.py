class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

s = "A man, a plan, a canal: Panama"
ss = Solution()
print(ss.isPalindrome(s))
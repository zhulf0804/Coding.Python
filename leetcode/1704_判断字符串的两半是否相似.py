class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        tar = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a, b = 0, 0
        for i in range(n // 2):
            if s[i] in tar:
                a += 1
        for i in range(n // 2, n):
            if s[i] in tar:
                b += 1
        if a == b:
            return True
        else:
            return False
a = Solution()
print(a.halvesAreAlike("textbook"))
class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return 0
        alphas = [chr(i) for i in range(65, 65 + 26)]
        summ = alphas.index(s[0]) + 1
        for i in range(1, len(s)):
            summ = summ * 26 + alphas.index(s[i]) + 1
        return summ
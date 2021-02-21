class Solution:
    def countHomogenous(self, s: str) -> int:
        ans, n = 0, len(s)
        i, j = 0, 0
        while j < n:
            if s[i] == s[j]:
                ans += (j - i + 1)
                ans = ans % (1e9 + 7)
                j += 1
            else:
                i = j

        return int(ans)
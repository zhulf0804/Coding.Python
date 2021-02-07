class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return S
        n = len(S)
        res, i, j = '', 0, 0
        while j < n:
            if S[i] == S[j]:
                j += 1
            else:
                res += S[i] + str(j - i)
                i = j
        res += S[i] + str(j - i)
        if len(res) >= n:
            return S
        return res

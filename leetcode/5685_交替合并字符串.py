class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i, j, flag = 0, 0, 0
        s = ''
        while i < n or j < m:
            if i >= n:
                s += word2[j]
                j += 1
                continue
            if j >= m:
                s += word1[i]
                i += 1
                continue
            if flag % 2 == 0:
                s += word1[i]
                i += 1
            else:
                s += word2[j]
                j += 1
            flag += 1

        return s